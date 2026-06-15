from database import Session, User, Business, Review, Bookmark

from sqlalchemy import select
from datetime import date, datetime

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

# from app_session import app_session



# Adds a new user to User table and returns its id
def add_user(username, password):
    with Session() as session:
        with session.begin():
            new_user = User(username=username, password_hash=generate_password_hash(password), created_on=date.today())
            session.add(new_user)
            session.flush()
            
            return new_user.id
   
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

def generate_user_report(user_id):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"UserReport_{timestamp}.pdf"

    with Session() as session:
        user = session.get(User, user_id)

        businesses_stmt = select(Business).where(Business.owner_id == user_id)
        businesses_list = session.execute(businesses_stmt).scalars()

        reviews_stmt = select(Review).where(Review.user_id == user_id)
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
                    ["Rating", str(b.avg_rating)],
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
                b = session.get(Business, r.business_id)
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



def toggle_bookmark(user_id, business_id):
    with Session() as session:
        with session.begin():
            bookmark = session.get(Bookmark, (user_id, business_id))
            if bookmark:
                session.delete(bookmark)
            else:
                new_bookmark = Bookmark(user_id=user_id, business_id=business_id)
                session.add(new_bookmark)

# Returns a set of all the business ids a user has bookmarked
def get_users_bookmarks(user_id):
    with Session() as session:
        stmt = select(Bookmark.business_id).where(Bookmark.user_id == user_id)

        return set(session.scalars(stmt).all())


def check_if_bookmark(user_id, business_id):
    with Session() as session:
        with session.begin():
            bookmark = session.get(Bookmark, (user_id, business_id))
            if bookmark:
                return True
            else:
                return False

