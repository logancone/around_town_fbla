from database import Session, Business, Review, Bookmark, Tag, BusinessTag

from sqlalchemy import select, func
from datetime import date

from rapidfuzz.distance import DamerauLevenshtein

from geopy.distance import great_circle

# Business services include any database queries/updates that mainly pertain to businesses

# Adds a new business to Business table
def add_business(name: str, owner_id: int, category: str, thumbnail_link: str, business_description:str, lat: float, lon: float):
    """Adds a new business to the Business table.

    Args:
        name (str): The name of the business.
        owner_id (int): The user_id of the business owner.
        category (str): The category of the business (must be 'food', 'retail', 'entertainment', or 'services').
        thumbnail_link (str): The path to the desired business thumbnail (usually begins with resources/images/business_thumbnails/).
        business_description (str): The description for the business.
        lat (float): The latitude of the business.
        lon (float): The longitude of the business.

    """
    with Session() as session:
        with session.begin():
            new_business = Business(name=name, owner_id=owner_id, category=category, thumbnail_link=thumbnail_link, business_description=business_description, lat=lat, lon=lon)
            session.add(new_business)

# Adds a new review to Review table
def add_review(user_id: int, business_id: int, rating: float, content: str):
    """Adds a new review to the Review table.

    Args:
        user_id (int): The user_id of the reviewer.
        business_id (int): The business_id of the business being reviewed.
        rating (float): The rating the user gave the business (0-5).
        content (str): The contents of the user's review.
    
    Raises:
        AssertionError: If business_id doesn't correspond to a real business in the database.
    """
    with Session() as session:
        with session.begin():
            new_review = Review(user_id=user_id, business_id=business_id, rating=rating, content=content, timestamp=date.today())
            session.add(new_review)
            session.flush()

            # Get average rating and rating count
            stmt = select(func.avg(Review.rating).label('rating'), 
                    func.count(Review.rating).label('num')
                    ).where(Review.business_id == business_id)
        
            result = session.execute(stmt).one_or_none()

            business = session.get(Business, business_id)

            assert business and result

            business.avg_rating = round(result.rating, 1)
            business.rating_count = result.num
            
def get_all_businesses() -> list[Business]:
    """Retreives a list of all Business objects from the database.

    Returns:
        list[Business]: A list of every Business object in the Business table.
    """
    with Session() as session:
        # Get all businesses
        businesses = session.scalars(select(Business)).all()
        return list(businesses)

# Returns all reviews for a certain business id
def get_reviews_for_business(business_id: int) -> list[Review]:
    """Retrieves all reveiws for a certain business.

    Args:
        business_id (int): The id of the business that contains the desired reviews.
    
    Returns:
        list[Review]: A list of Review objects with the corresponding buisness_id
    """
    with Session() as session:
        stmt = select(Review).where(Review.business_id == business_id)
        reviews = session.scalars(stmt).all()
        return list(reviews)

def add_preset_tag(tag_name: str):
    """Creates a new preset tag with a given tag_name

    Args:
        tag_name (str): The name of the new tag
    """
    with Session() as session:
        with session.begin():
            new_tag = Tag(tag_name=tag_name)
            session.add(new_tag)

def set_business_tag(business_id: int, tag_id: int):
    """Adds a tag to a business.

    Args:
        business_id (int): The id of the business adding the tag.
        tag_id (int): The id of the tag to be added.
    """
    with Session() as session:
        with session.begin():
            new_btag = BusinessTag(business_id=business_id, tag_id=tag_id)
            session.add(new_btag)

def get_tags_from_business(business_id: int, names=False) -> list: 
    """Gets all the tags from a specific business ID.

    Args:
        business_id (int): The ID of the business to search for.
        names (bool, optional): If True, returns a list of tag names (strings). 
            If False, returns a list of tag ids. Defaults to False.

    Returns:
        list[int | str]: A list containing the tag ids or their names 
        associated with the business.

    Raises:
        AssertionError: If a tag associated with the business cannot be found 
            in the Tag database table.
    """
    with Session() as session:
        stmt = select(BusinessTag).where(BusinessTag.business_id == business_id)
        tags = session.scalars(stmt)
        tag_list = []
        for tag in tags:
            t = session.get(Tag, tag.tag_id)
            
            assert t

            if names:
                tag_list.append(t.tag_name)
            else:
                tag_list.append(t.id)

        return tag_list

def get_tag_from_id(tag_id: int) -> str:
    """ Gets the name of a specific tag

    Args:
        tag_id (int): The id of the tag.

    Returns:
        str: The name of the tag with the given id

    Raises:
        AssertionError: If tag_id does not exist in the Tag data table.
    """
    with Session() as session:
        tag = session.get(Tag, tag_id)
        assert tag
        return tag.tag_name

def run_search(query: str, business_list: list[Business]) -> list[Business]:
    """Runs a search with a given query on a list of businesses.

    Retrieves the most relevant businesses. Utilizes a multi-stage search algorithm,
    including business title, tags, category, and description. Also, 
    uses Damerau-Levenshtein string similarity metric for typo-detection. 
    Only businesses above a certain dynamic threshold are returned.

    Args:
        query (str): The search input.
        business_list (list[Business]): A list of business objects to search through.

    Returns:
        list[Business]: A list containing business objects of any matching businesses, 
            ranked by relevance to the search query
    """
    with Session() as session:
        query = query.lower()
        results = []
        for business in business_list:
            score = 0
            
            # Business Name
            if business.name.lower() == query:
                score += 1000
            elif business.name.lower().startswith(query):
                score += 100
            elif any(word.startswith(query) for word in business.name.lower().split()):
                score += 80


            # Fuzzy name backup
            if len(query) >= 3:
                score += max(DamerauLevenshtein.normalized_similarity(query, word) for word in business.name.lower().split()) * 15

            # Tags
            best_tag_score = 0
            for tag in get_tags_from_business(business.id, True):
                if tag.lower() == query:
                    score += 75
                
                best_tag_score = max(best_tag_score, DamerauLevenshtein.normalized_similarity(query, tag.lower()))

            score += best_tag_score * 20
            
            # Description
            description_words = business.business_description.lower().split()
            if query in description_words:
                score += 10

            # Category
            if len(query) >= 3:
                score += DamerauLevenshtein.normalized_similarity(query, business.category.lower()) * 10

            results.append((score, session.get(Business, business.id)))

        # Sort all results by their score to determine max score
        results.sort(reverse=True, key=lambda x: x[0])
        max_score = results[0][0]
        business_data_list: list[Business] = []

        # Only add items that are within 30% of max value (or above 25 if all scores are low)
        for item in results:
            if item[0] >= max(max_score * 0.3, 25):
                business_data_list.append(item[1])

        return business_data_list

def get_business_from_id(business_id: int) -> Business | None:
    """Returns the Business object from a given id.

    Args:
        business_id (int): The id of the desired business.

    Returns:
        Business | None: Returns the Business object matching the business_id, if it exists. Else, returns None.
    """
    with Session() as session:
        return session.get(Business, business_id)
    
def get_distance_to_business(business_id: int, user_lat: float, user_lon: float) -> float:
    """Caclulates the distance between a business and a set of coordinates.

    Args:
        business_id (int): The id of the desired business.
        user_lat (float): The current latitude coordinate of the user.
        user_lon (float): The current longitude coordinate of the user.

    Returns:
        float: The distance between the business and the user in miles (unrounded).

    Raises:
        AssertionError: If the business_id does not exist.
    """
    with Session() as session:
        b = session.get(Business, business_id)
        assert b

        user_coords = (user_lat, user_lon)
        business_coords = (b.lat, b.lon)
        
        dist = great_circle(user_coords, business_coords)

        return dist.miles