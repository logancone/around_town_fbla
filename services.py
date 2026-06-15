from database import Session, User, Business, Review, Bookmark, Tag, BusinessTag

from sqlalchemy import select, func
from datetime import date, datetime
from dataclasses import dataclass

from werkzeug.security import generate_password_hash, check_password_hash

import sys
import os
import subprocess


from reportlab.platypus import (
SimpleDocTemplate,
Paragraph,
Spacer,
Table,
TableStyle,
Image,
PageBreak
)

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

from rapidfuzz.distance import DamerauLevenshtein
from rapidfuzz import fuzz

# Classes

# AppSession class stores pertinent session information, such as the active user_id and current business_id
class AppSession():
    def __init__(self):
        # self.user_id = -1
        self.user_id = 1
        self.business_id = -1

    def set_user_id(self, new_id):
        self.user_id = new_id

    def get_user_id(self):
        return self.user_id
    
    def logout_user(self):
        self.user_id = -1
    
    def set_business_id(self, new_id):
        self.business_id = new_id
    
    def get_business_id(self):
        return self.business_id
    
    def leave_business(self):
        self.business_id = -1

# BusinessData class stores all business information including bookmark and rating info to avoid excessive db queries when loading business cards
@dataclass
class BusinessData:
    id: int
    name:str
    category:str
    thumbnail_link:str
    rating:float
    rating_str:str
    bookmarked:bool
    business_description:str
    lat:float
    lon:float

# Methods

# Adds a new user to User table and returns its id
def add_user(username, password):
    with Session() as session:
        with session.begin():
            new_user = User(username=username, password_hash=generate_password_hash(password), created_on=date.today())
            session.add(new_user)
            session.flush()
            
            return new_user.id
    
# Adds a new business to Business table
def add_business(name, owner_id, category, thumbnail_link, business_description, lat, lon):
    with Session() as session:
        with session.begin():
            new_business = Business(name=name, owner_id=owner_id, category=category, thumbnail_link=thumbnail_link, business_description=business_description, lat=lat, lon=lon)
            session.add(new_business)

# Adds a new review to Review table
def add_review(user_id, business_id, rating, content):
    with Session() as session:
        new_review = Review(user_id=user_id, business_id=business_id, rating=rating, content=content, timestamp=date.today())
        session.add(new_review)
        session.commit()

        # Calculate avg rating
        stmt = select(func.avg(Review.rating)).where(Review.business_id == business_id)
        avg = session.scalar(stmt)

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
        if user and check_password_hash(user.password_hash, password):
            return user
        else:
            return None

# Pulls business, rating, and bookmark data for every business, returning a list of BusinessData objects for every business in the database
def get_all_business_data():
    user_id = app_session.get_user_id()

    with Session() as session:
        # Get all businesses
        businesses = session.scalars(select(Business)).all()

        # Pull rating information
        rating_stmt = (
            select(
                Review.business_id,
                func.avg(Review.rating),
                func.count(Review.id)
            )
            .group_by(Review.business_id)
        )

        rating_results = session.execute(rating_stmt).all()

        # Organize rating info into dictionary
        ratings_map = {
            row[0]: (float(row[1]), row[2])
            for row in rating_results
        }
        
        # Pull bookmark information
        bookmark_stmt = select(Bookmark.business_id).where(
            Bookmark.user_id == user_id
        )

        bookmarked_ids = set(session.scalars(bookmark_stmt).all())

    business_data_list = []

    # Organize data into BusinessData classes and return
    for b in businesses:
        avg, count = ratings_map.get(b.id, (0.0, 0))

        rating_str = f"⭐{avg:.1f} ({count})" if count > 0 else "No reviews"

        business_data_list.append(
            BusinessData(
                id=b.id,
                name=b.name,
                category=b.category,
                thumbnail_link=b.thumbnail_link,
                rating=avg,
                rating_str=rating_str,
                bookmarked=b.id in bookmarked_ids,
                business_description=b.business_description,
                lat=b.lat,
                lon=b.lon
            )
        )

    return business_data_list
    
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
    with Session() as session:
        # Sweitch to session.get
        stmt = select(User).where(User.id == user_id)
        user = session.scalars(stmt).one_or_none()

        if user != None:
            return user.username
        else:
            return None

def is_username_available(username):
    with Session() as session:
        stmt = select(User).where(User.username == username)
        user = session.scalars(stmt).first()

        if user is None:
            return True
        else:
            return False

def toggle_bookmark(user_id, business_id):
    with Session() as session:
        with session.begin():
            bookmark = session.get(Bookmark, (user_id, business_id))
            if bookmark:
                session.delete(bookmark)
            else:
                new_bookmark = Bookmark(user_id=user_id, business_id=business_id)
                session.add(new_bookmark)

def get_bookmarks_by_user(user_id):
    with Session() as session:
        stmt = select(Bookmark).where(Bookmark.user_id == user_id)
        return session.scalars(stmt).all()

def get_business_data_from_id(business_id):
    user_id = app_session.user_id

    with Session() as session:
        b = session.get(Business, business_id)
        rating_stmt = (
            select(
                Review.business_id,
                func.avg(Review.rating),
                func.count(Review.id)
            )
            .group_by(Review.business_id)
        )

        rating_results = session.execute(rating_stmt).all()

        ratings_map = {
            row[0]: (float(row[1]), row[2])
            for row in rating_results
        }

        bookmark_stmt = select(Bookmark.business_id).where(
            Bookmark.user_id == user_id
        )

        bookmarked_ids = set(session.scalars(bookmark_stmt).all())
        assert b

        avg, count = ratings_map.get(b.id, (0.0, 0))

        rating_str = f"⭐{avg:.1f} ({count})" if count > 0 else "No reviews"

        return BusinessData(
                id=b.id,
                name=b.name,
                category=b.category,
                thumbnail_link=b.thumbnail_link,
                rating=avg,
                rating_str=rating_str,
                bookmarked=b.id in bookmarked_ids,
                business_description=b.business_description,
                lat=b.lat,
                lon=b.lon
        )

def check_if_bookmark(user_id, business_id):
    with Session() as session:
        with session.begin():
            bookmark = session.get(Bookmark, (user_id, business_id))
            if bookmark:
                return True
            else:
                return False


def generate_user_report():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"UserReport_{timestamp}.pdf"

    with Session() as session:
        user = session.get(User, app_session.get_user_id())

        businesses_stmt = select(Business).where(Business.owner_id == app_session.user_id)
        businesses_list = session.execute(businesses_stmt).scalars()

        reviews_stmt = select(Review).where(Review.user_id == app_session.user_id)
        reviews_list = session.execute(reviews_stmt).scalars()

        assert user

        doc = SimpleDocTemplate(filename, pagesize=letter)
        styles = getSampleStyleSheet()

        elements = []

        # Title (username)
        elements.append(Paragraph(f"<b>User Report: {user.username}</b>", styles["Heading1"]))
        elements.append(Spacer(1, 12))

        # User info
        elements.append(Paragraph("<b>User Information</b>", styles["Heading2"]))
        elements.append(Spacer(1, 6))

        user_info_table = Table([
            ["Username", user.username],
            ["Created Date", str(user.created_on)]
        ])

        user_info_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ]))

        elements.append(user_info_table)
        elements.append(Spacer(1, 20))

        # Owned Businessess
        elements.append(Paragraph("<b>Owned Businesses</b>", styles["Heading2"]))
        elements.append(Spacer(1, 10))

        if not businesses_list:
            elements.append(Paragraph("No businesses owned.", styles["BodyText"]))
        else:
            for b in businesses_list:
                elements.append(Paragraph(f"<b>{b.name}</b>", styles["Heading3"]))
                elements.append(Spacer(1, 5))

                # thumbnail image (optional fail-safe)
                try:
                    img = Image(b.thumbnail_link, width=80, height=80)
                    elements.append(img)
                except:
                    pass

                biz_table = Table([
                    ["Category", b.category],
                    ["Rating", str(b.rating)],
                    ["Description", Paragraph(b.business_description, styles["BodyText"])],
                ])

                biz_table.setStyle(TableStyle([
                    ("BOX", (0, 0), (-1, -1), 1, colors.black),
                    ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ]))

                elements.append(biz_table)
                elements.append(Spacer(1, 15))

        elements.append(PageBreak())

        # User reviews
        elements.append(Paragraph("<b>User Reviews</b>", styles["Heading1"]))
        elements.append(Spacer(1, 10))

        if not reviews_list:
            elements.append(Paragraph("No reviews posted.", styles["BodyText"]))
        else:
            for r in reviews_list:
                b = get_business_data_from_id(r.business_id)
                assert b
                elements.append(Paragraph(f"<b>{b.name}</b>", styles["Heading3"]))
                elements.append(Paragraph(f"Rating: ⭐ {r.rating}", styles["BodyText"]))
                elements.append(Spacer(1, 4))
                elements.append(Paragraph(r.content, styles["BodyText"]))
                elements.append(Spacer(1, 12))

        # Build
        doc.build(elements)

        open_file(filename)

def open_file(path):
    if sys.platform.startswith("win"):
        os.startfile(path)
    elif sys.platform.startswith("darwin"):
        subprocess.call(["open", path])
    else:
        subprocess.call(["xdg-open", path])

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

def get_tags_from_business(business_id):
    with Session() as session:
        stmt = select(BusinessTag).where(BusinessTag.business_id == business_id)
        tags = session.scalars(stmt)
        tag_list = []
        for tag in tags:
            t = session.get(Tag, tag.tag_id)
            
            assert t

            tag_list.append(t.tag_name)

        return tag_list


def run_search(query):
    with Session() as session:
        query = query.lower()
        stmt = select(Business)
        results = []
        for business in session.scalars(stmt):
            score = 0
            
            # Name
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
            for tag in get_tags_from_business(business.id):
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

            results.append((score, get_business_data_from_id(business.id)))

        results.sort(reverse=True, key=lambda x: x[0])
        business_data_list = []
        max_score = results[0][0]

        for item in results:
            if item[0] >= max(max_score * 0.3, 25):
                business_data_list.append(item[1])

        return business_data_list

            

            
            

            
            


# Initializes an instance of the AppSession class to store relevant info
app_session = AppSession()

