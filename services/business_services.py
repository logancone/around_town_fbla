from database import Session, Business, Review, Bookmark, Tag, BusinessTag

from sqlalchemy import select, func
from datetime import date

from rapidfuzz.distance import DamerauLevenshtein

from geopy.distance import great_circle

# Business services include any database queries/updates that mainly pertain to businesses

# Adds a new business to Business table
def add_business(name, owner_id, category, thumbnail_link, business_description, lat, lon):
    with Session() as session:
        with session.begin():
            new_business = Business(name=name, owner_id=owner_id, category=category, thumbnail_link=thumbnail_link, business_description=business_description, lat=lat, lon=lon)
            session.add(new_business)

# Adds a new review to Review table
def add_review(user_id, business_id, rating, content):
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
            
   
# UPDATE THIS
# Pulls business, rating, and bookmark data for every business, returning a list of BusinessData objects for every business in the database
def get_all_businesses():
    with Session() as session:
        # Get all businesses
        businesses = list(session.scalars(select(Business)).all())
        return businesses
    
# Update
# Returns all reviews for a certain business id
def get_reviews_for_business(business_id):
    session = Session()
    
    stmt = select(Review).where(Review.business_id == business_id)
    reviews = session.scalars(stmt).all()
    session.close()
    return reviews

# Returns avg rating (num of ratings) for a certain business id as a string
def get_rating_str(business_id):
    session = Session()

    stmt = select(func.avg(Review.rating).label('rating'), 
                  func.count(Review.rating).label('num')
                  ).where(Review.business_id == business_id)
    
    result = session.execute(stmt).one_or_none()
    session.close()
    if result is not None:
        return f"⭐{round(result.rating, 1)} ({result.num})"
    else:
        return f"⭐None (0)"

def add_preset_tag(tag):
    with Session() as session:
        with session.begin():
            new_tag = Tag(tag_name=tag)
            session.add(new_tag)

def set_business_tag(business_id, tag_id):
    with Session() as session:
        with session.begin():
            new_btag = BusinessTag(business_id=business_id, tag_id=tag_id)
            session.add(new_btag)

def get_tags_from_business(business_id: int, names=False): 
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

def get_tag_from_id(tag_id):
    with Session() as session:
        tag = session.get(Tag, tag_id)
        assert tag
        return tag.tag_name

def run_search(query: str, business_list: list[Business]) -> list[Business]:
    """Runs a search with a given query on a list of businesses, retrieving the
        most relevant businesses. Utilizes a multi-stage search algorithm, including business
        title, tags, category, and description. Also, uses Damerau-Levenshtein string similarity
        metric for typo-detection. Only businesses above a certain dynamic threshold are returned.

    Args:
        query (str): The search input
        business_list (list[Business]): A list of business objects to search through

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


def get_business_from_id(business_id):
    with Session() as session:
        return session.get(Business, business_id)
    

def get_distance_to_business(business_id, user_lat, user_lon):
    with Session() as session:
        b = session.get(Business, business_id)
        assert b

        user_coords = (user_lat, user_lon)
        business_coords = (b.lat, b.lon)
        
        dist = great_circle(user_coords, business_coords)

        return dist.miles