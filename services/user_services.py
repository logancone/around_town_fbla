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

from dataclasses import dataclass, field

from services.business_services import get_tags_from_business, get_business_from_id, get_tag_from_id, get_all_businesses


from dotenv import load_dotenv
from openai import OpenAI   

from PySide6.QtCore import QThread, Signal

import json

# User services include any database queries/updates that mainly pertain to the user

# Adds a new user to User table and returns its id, storing the password as a hash
def add_user(username, password, lat, lon):
    """Adds a new user to the User table.
    
    Returns:
        The user_id for the newly added user
    """
    with Session() as session:
        with session.begin():
            new_user = User(username=username, password_hash=generate_password_hash(password), lat=lat, lon=lon, created_on=date.today())
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

# Takes in a user_id and returns the user(if exists, else none)
def get_username_from_id(user_id):
    with Session() as session:
        user = session.get(User, user_id)

        if user != None:
            return user.username
        else:
            return None

# Checks to see if any users have a specific username, returns true if so 
def is_username_available(username):
    with Session() as session:
        stmt = select(User).where(User.username == username)
        user = session.scalars(stmt).first()

        if user is None:
            return True
        else:
            return False

def generate_user_report(user_id, user_info: bool, bookmarked_businesses: bool, owned_businesses: bool, review_history: bool):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"UserReport_{timestamp}.pdf"

 
    user = get_user_from_id(user_id)

    bookmarked_businesses_list = get_users_bookmarked_businesses(user_id)
    owned_businesses_list = get_users_owned_businesses(user_id)
    reveiws_list = get_users_reviews(user_id)

    assert user

    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()

    elements = []

    # Title (username)
    elements.append(Paragraph(f"<b>User Report: {user.username}</b>", styles["Heading1"]))
    elements.append(Spacer(1, 12))

    # User info
    if user_info:
        elements.append(Paragraph("<b>User Information</b>", styles["Heading2"]))
        elements.append(Spacer(1, 6))

        user_info_table = Table([
            ["Username", user.username],
            ["Created Date", str(user.created_on)],
            ["Latitude", user.lat],
            ["Longitude", user.lon]

        ])

        user_info_table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("INNERGRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ]))

        elements.append(user_info_table)
        elements.append(Spacer(1, 50))

    if bookmarked_businesses:
        elements.append(Paragraph("<b>Bookmarked Businesses</b>", styles["Heading2"]))
        elements.append(Spacer(1, 10))

        if not bookmarked_businesses_list:
            elements.append(Paragraph("No businesses bookmarked.", styles["BodyText"]))
        else:
            for b in bookmarked_businesses_list:
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
            
        elements.append(Spacer(1, 50))
    
    # Owned Businessess
    if owned_businesses:
        elements.append(Paragraph("<b>Owned Businesses</b>", styles["Heading2"]))
        elements.append(Spacer(1, 10))

        if not owned_businesses_list:
            elements.append(Paragraph("No businesses owned.", styles["BodyText"]))
        else:
            for b in owned_businesses_list:
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

        elements.append(Spacer(1, 50))

        

    # User reviews
    if review_history:
        elements.append(Paragraph("<b>User Reviews</b>", styles["Heading1"]))
        elements.append(Spacer(1, 10))

        if not reveiws_list:
            elements.append(Paragraph("No reviews posted.", styles["BodyText"]))
        else:
            for r in reveiws_list:
                b = get_business_from_id(r.business_id)
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
def get_users_bookmarked_business_ids(user_id: int) -> set[int]:
    with Session() as session:
        stmt = select(Bookmark.business_id).where(Bookmark.user_id == user_id)

        return set(session.scalars(stmt).all())

def get_users_bookmarked_businesses(user_id:int) -> list[Business]:
    with Session() as session:
        stmt = select(Business).join(Bookmark, Bookmark.business_id == Business.id).where(Bookmark.user_id == user_id)
        
        businesses = list(session.scalars(stmt).all())
        return businesses

def check_if_bookmark(user_id, business_id):
    with Session() as session:
        with session.begin():
            bookmark = session.get(Bookmark, (user_id, business_id))
            if bookmark:
                return True
            else:
                return False

def get_users_reviews(user_id):
    with Session() as session:
        stmt = select(Review).where(Review.user_id == user_id)

        return session.scalars(stmt).all()

def get_users_owned_businesses(user_id: int) -> list[Business]:
    with Session() as session:
        stmt = select(Business).where(Business.owner_id == user_id)
        businesses = list(session.scalars(stmt).all())
        return businesses

def get_user_from_id(user_id: int) -> User:
    with Session() as session:
        user = session.get(User, user_id)
        assert user
        return user

def update_user_location(user_id: int, new_lat: float, new_lon: float):
    with Session() as session:
        with session.begin():
            user = session.get(User, user_id)
            assert user
            user.lat = new_lat
            user.lon = new_lon

# Create a class to score recommendation data (tags/categories and matching scores)
class RecommendationService:

    def __init__(self, user_id: int | None):
        self.user_id = user_id
        self.tag_scores: dict[int, float] = {}
        self.category_scores: dict[str, float] = {}
        self.sorted_businesses = []

        if self.user_id is not None:
            self.build_profile()
            self.sort_all_businesses_by_rec_score()

    # Clears recommendation profile
    def clear(self):
        self.tag_scores.clear()
        self.category_scores.clear()
        self.sorted_businesses.clear()

    # Goes through users reviews to build a new recommendation profile
    def build_profile(self):
        self.clear()
        assert self.user_id

        reviews = get_users_reviews(self.user_id)
        bookmark_ids = get_users_bookmarked_business_ids(self.user_id)

        for review in reviews:
            # Assigns the tag score appropriately (5=2, 4=1, 3=0, 2=-0.25, 1=-0.5, etc.) and works for half star ratings
            preference_score = 0
            if review.rating >= 3:
                preference_score = review.rating - 3
            else:
                preference_score = (review.rating - 3) * 0.25

            tags = get_tags_from_business(review.business_id)
            for tag in tags:
                self.tag_scores[tag] = self.tag_scores.get(tag, 0) + preference_score
            
            b = get_business_from_id(review.business_id)
            assert b is not None
            
            category = b.category
            self.category_scores[category] = self.category_scores.get(category, 0) + preference_score
        
        for id in bookmark_ids:
            tags = get_tags_from_business(id)
            for tag in tags:
                self.tag_scores[tag] = self.tag_scores.get(tag, 0) + 1.5
            
            b = get_business_from_id(id)
            assert b is not None
            
            category = b.category
            self.category_scores[category] = self.category_scores.get(category, 0) + 1.5

    def get_recommendation_score(self, business_id):
        reviewed_ids = {review.business_id for review in get_users_reviews(self.user_id)}
        if business_id in reviewed_ids:
            return 0

        b = get_business_from_id(business_id)
        assert b
        
        category_score = self.category_scores.get(b.category, 0)

        tags = get_tags_from_business(business_id)
        
        tag_sum = 0
        for tag in tags:
            tag_sum += self.tag_scores.get(tag, 0)

        tag_score = tag_sum/(len(tags) ** 0.5)

        total_score = tag_score + (category_score * 0.25)
        return total_score
    
    def sort_all_businesses_by_rec_score(self):
        all_businesses = get_all_businesses()
        self.sorted_businesses = sorted(all_businesses, key=lambda b:self.get_recommendation_score(b.id))
        return self.sorted_businesses
    
    def sort_some_businesses_by_rec_score(self, businesses):
        sorted_businesses = sorted(businesses, key=lambda b:self.get_recommendation_score(b.id))
        return sorted_businesses
    
    def create_ai_context_file(self):
        top_positive_tags = [
            {"tag": get_tag_from_id(k), "score": v}
            for k, v in sorted(self.tag_scores.items(),
                            key=lambda item: item[1],
                            reverse=True)
            if v > 0
        ][:5]
        top_negative_tags = [
            {"tag": get_tag_from_id(k), "score": v}
            for k, v in sorted(self.tag_scores.items(),
                            key=lambda item: item[1])
            if v < 0
        ][:3]
        
        top_business_recs = [
            {"name": b.name, "tags": get_tags_from_business(b.id, names=True)}
            for b in self.sorted_businesses
        ][:5]

        all_businesses = get_all_businesses()
        all_business_names = [
            {"name": b.name, "id": b.id}
            for b in all_businesses
        ]

        context = {
            "user_profile": {
                "favorite tags" : top_positive_tags,
                "disliked tags": top_negative_tags,
                "category_info": self.category_scores
            },
            "top_business_recommendations" : top_business_recs,
            "all_business_names" : all_business_names
        }

        json_string = json.dumps(context)
        return json_string



# AI STUFF
class AIService:
    def __init__(self):
        self.messages = []
        # self.cur_message = ""

        load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # def get_model_context(self, rec_service: RecommendationService):
    #     self.cur_message = "You are a recommendation agent for an application, AroundTown, where users can find local small businesses."

    def send_chat(self, chat: str, rec_service: RecommendationService):
        assert len(chat) > 0 and len(chat) < 1000
        self.messages.append(chat)

        context = json.loads(rec_service.create_ai_context_file())

        context["user_query"] = chat
        context["message_history"] = self.messages[-7:-1]

        final_input = json.dumps(context)


        reasoning_level = self.decide_reasoning_level(chat)
        verbosity = self.decide_verbosity(chat)

        print(f"Reasoning: {reasoning_level} | Verbosity: {verbosity}")

        response = self.client.responses.create(
            model="gpt-5-nano",
            instructions="You are a recommendation assistant for an application, AroundTown, where users can find local small businesses. " \
            "Use only provided data, and do not invent facts. Respond directly to user requests. ONLY give recommendations when directly asked " \
            "Keep responses relatively concise. Avoid repetition. Don't ask a question you cannot answer, such as offering directions " \
            "Avoid telling users tags and ids unless neccessary for explanation, they are more for internal reasoning. " \
            "If a user requests more detailed information about one or more specific businesses, respond ONLY with valid JSON in this exact format: " \
            "{\"action\":\"get_business_info\",\"businesses\":[<business_ids>]} where business_ids is an array of up to 3 business IDs from the provided business name/id list. " \
            "Only use IDs that are explicitly included in the provided list. Do not invent, modify, or guess any IDs. " \
            "If no valid business ID/name is mentioned, do not use this action and respond normally instead. Output ONLY the JSON object and nothing else.",
            input=final_input,
            reasoning={
                "effort": reasoning_level # type: ignore
            },
            text={
                "verbosity": verbosity # type: ignore
            }
        )

        self.messages.append(response.output_text)

        if response.output_text.strip().startswith("{"):
            return self.ai_data_request(response.output_text.strip(), final_input)
        else:
            return response.output_text
    
    def decide_reasoning_level(self, message: str) -> str:
        msg = message.lower().strip()

        # very short + no real content
        if len(msg) < 10:
            return "minimal"

        # questions that require explanation or reasoning
        if any(k in msg for k in [
            "why", "explain", "how", "compare",
            "vs", "difference", "should i"
        ]):
            return "low"

        # recommendation / decision queries
        if any(k in msg for k in [
            "recommend", "suggest", "best", "what",
            "where", "place", "restaurant", "business"
        ]):
            return "low"

        return "low"
    
    def decide_verbosity(self, message: str) -> str:
        msg = message.lower()

        if any(k in msg for k in ["detailed", "in depth", "full explanation", "detail"]):
            return "high"
        
        if any(k in msg for k in ["explain", "why", "compare", "how"]):
            return "medium"

        return "low"

    def ai_data_request(self, ai_json, input):
        try:
            obj = json.loads(ai_json)

            if obj.get("action") == "get_business_info" and isinstance(obj.get("businesses"), list):
                detailed_business_info = {}
                for b_id in obj.get("businesses"):
                    b = get_business_from_id(b_id)
                    assert b
                    b_info = {}
                    b_info["Category"] = b.category
                    b_info["Tags"] = get_tags_from_business(b.id)
                    b_info["Description"] = b.business_description
                    b_info["Rating"] = b.avg_rating
                    detailed_business_info[b.name] = b_info

                # SEND TO AI AGAIN
                context = json.loads(input)

                context["detailed_business_information"] = detailed_business_info

                final_input = json.dumps(context)

                reasoning_level = 'low'
                verbosity = 'medium'

                response = self.client.responses.create(
                    model="gpt-5-nano",
                    instructions="You are a recommendation agent for an application, AroundTown, where users can find local small businesses. " \
                    "Use only provided data, and do not invent facts. Respond directly to user requests and only give recommendations when asked " \
                    "Keep responses relatively concise. Avoid repetition. Don't ask a question you cannot answer, such as offering directions " \
                    "Avoid telling users tags unless neccessary for explanation, they are more for internal reasoning. " \
                    "Use the provided detailed business information to answer the user's request. " \
                    "Be concise and explain clearly why the business matches their query.",
                    input=final_input,
                    reasoning={
                        "effort": reasoning_level # type: ignore
                    },
                    text={
                        "verbosity": verbosity # type: ignore
                    }
                )

                self.messages.append(response.output_text)
                return response.output_text
            else:
                return ai_json
        except json.JSONDecodeError:
            return ai_json

class AIWorker(QThread):
    finished = Signal(str)
    error = Signal(str)

    def __init__(self, ai_service: AIService, message: str, rec_service: RecommendationService):
        super().__init__()
        self.ai_service = ai_service
        self.message = message
        self.rec_service = rec_service
    
    def run(self):
        try:
            response = self.ai_service.send_chat(self.message, self.rec_service)
            self.finished.emit(response)

        except Exception as e:
            self.error.emit(str(e))
        