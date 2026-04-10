from database import Session, User, Business, Review, Bookmark

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

# Adds a new user to User table and returns its id
def add_user(username, password):
    with Session() as session:
        with session.begin():
            new_user = User(username=username, password_hash=generate_password_hash(password), created_on=date.today())
            session.add(new_user)
            session.flush()
            
            return new_user.id
    
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
        if user and check_password_hash(user.password_hash, password):
            return user
        else:
            return None

def get_all_business_data():
    user_id = app_session.get_user_id()

    with Session() as session:
        businesses = session.scalars(select(Business)).all()

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

    business_data_list = []

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
                business_description=b.business_description
            )
        )

    return business_data_list
    
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
                business_description=b.business_description
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

app_session = AppSession()

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
