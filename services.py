from database import Session, User, Business, Review

from sqlalchemy import select, func
from datetime import date

# Adds a new user to User table
def add_user(username, password):
    session = Session()
    
    new_user = User(username=username, password=password, created_on=date.today())
    session.add(new_user)
    session.commit()
    session.close()

# Adds a new business to Business table
def add_business(name, owner_id, category, thumbnail_link, business_description):
    session = Session()

    new_business = Business(name=name, owner_id=owner_id, category=category, thumbnail_link=thumbnail_link, business_description=business_description)
    session.add(new_business)
    session.commit()
    session.close()

# Adds a new review to Review table
def add_review(user_id, business_id, rating, content):
    with Session() as session:
        new_review = Review(user_id=user_id, business_id=business_id, rating=rating, content=content, timestamp=date.today())
        session.add(new_review)
        session.commit()

        # Calculate avg rating
        stmt = select(func.avg(Review.rating)).where(Review.business_id == business_id)
        avg = session.scalar(stmt)
        # stmt = select(Business).where(Business.id == business_id)
        business = session.get(Business, business_id)

        if business and avg is not None:
            business.rating = avg
        
        session.commit()
   

# Takes a username and password and checks if the combination exists in User table
def authenticate_user(username, password):
    # Open a new Session
    with Session() as session:
        # Search Users with this specific username
        stmt = select(User).where(User.username == username)
        user = session.scalars(stmt).first()

        # If user exists and password is correct, return the user. If not, return None
        if user and user.password == password:
            return user
        else:
            return None


def get_businesses_all():
    session = Session()

    stmt = select(Business)

    result = session.scalars(stmt).all()
    return result

def get_businesses_by_category(category):
    with Session() as session:
        stmt = select(Business).where(Business.category == category)
        result = session.scalars(stmt).all()
    
        return result
    
def sort_businesses_by_rating(ascending):
    with Session() as session:
        if ascending:
            stmt = select(Business).order_by(Business.rating)
        else:
            stmt = select(Business).order_by(Business.rating.desc())
        
        result = session.scalars(stmt).all()
        return result


# Returns all reviews for a certain business id
def get_reviews(business_id):
    session = Session()
    
    stmt = select(Review).where(Review.business_id == business_id)
    reviews = session.scalars(stmt).all()
    session.close()
    return reviews

# Returns avg rating (num of ratings) for a certain business id as a string
def get_rating_str(business_id):
    session = Session()

    stmt = select(func.avg(Review.rating).label('rating'), 
                  func.count(Review.rating).label('count')
                  ).where(Review.business_id == business_id)
    
    result = session.execute(stmt).one_or_none()
    session.close()
    if result is not None:
        return f"⭐{round(result.rating, 1)} ({result.count})"
    else:
        return f"⭐None (0)"
    


def get_username_from_id(user_id):
    session = Session()

    stmt = select(User).where(User.id == user_id)
    user = session.scalars(stmt).one()

    session.close()
    return user.username


def is_username_available(username):
    with Session() as session:
        stmt = select(User).where(User.username == username)
        user = session.scalars(stmt).first()

        if user is None:
            return True
        else:
            return False
