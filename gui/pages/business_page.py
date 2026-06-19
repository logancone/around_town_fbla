from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QSize, Signal
from PySide6.QtGui import QIcon

from database import Business
from services.business_services import get_tags_from_business, get_reviews
from services.user_services import check_if_bookmark, toggle_bookmark

from app_session import app_session

from gui.generated.ui_business_page import Ui_Form as business_page

from gui.widgets.review_icon import ReviewIcon
from gui.widgets.review_editor import ReviewEditor

# Represents the business page for the application, shows business details, reviews, etc. 
# There is only one business page, and it changes information depending on which business it is displaying 
# (as opposed to one page per business)
class BusinessPage(QWidget):
    # Creates a signal to alert the navshell if the user presses the 'x' button to return to the discover page
    return_pressed = Signal()
    
    # Initialize class and setup ui
    def __init__(self):
        super().__init__()
        self.ui = business_page()
        self.ui.setupUi(self)

        # Create a list of reviews to allow for easy review removal 
        self.review_list: list[ReviewIcon] = []

        self.unfilled_icon = QIcon("resources/images/icons/yellow_unfilled_bookmark.png")
        self.filled_icon = QIcon("resources/images/icons/yellow_filled_bookmark.png")

        self.ui.bookmark_button.setIconSize(QSize(32, 32))

        self.ui.add_review_button.clicked.connect(self.open_review_editor)
        self.ui.bookmark_button.clicked.connect(self.bookmark_toggle)
        self.ui.back_button.clicked.connect(self.return_pressed.emit)

    # Go through the business page and set all of its info to the current business
    def set_to_business(self, business: Business):
        self.ui.business_page_title.setText(business.name)
        self.ui.description.setText(business.business_description)
        
        # Create a string list of tags from the BusinessTag database
        tags = get_tags_from_business(business.id)
        tag_str = f"Tags: {tags.pop(0)}"
        for tag in tags:
            tag_str += f", {tag}"
        self.ui.tag_label.setText(tag_str)

        if check_if_bookmark(app_session.user_id, app_session.business_id):
            self.ui.bookmark_button.setIcon(self.filled_icon)
            self.ui.bookmark_button.setChecked(True)
        else:
            self.ui.bookmark_button.setIcon(self.unfilled_icon)

        self.load_reviews()

    # Removes all current reviews from the page
    def clear_reviews(self):
        for review in self.review_list:
            review.deleteLater()
        
        self.review_list.clear()
    
    # Clears and loads reviews based on the current business id from the app session
    def load_reviews(self):
        self.clear_reviews()
        reviews = get_reviews(app_session.get_business_id())

        for review in reviews:
            # Add each review icon to both a list and the ui element
            review_icon = ReviewIcon(review)
            self.ui.review_holder.addWidget(review_icon)
            self.review_list.append(review_icon)

    # Creates a pop-up for the user to write a review and refreshes review list when submitted
    def open_review_editor(self):
        editor = ReviewEditor()
        editor.accepted.connect(self.load_reviews)
        editor.exec()

    # Lets the user toggle their bookmark state and updates the button icon
    def bookmark_toggle(self):
        # Gets the current user state and active business from the session
        user_id = app_session.get_user_id()
        business_id = app_session.get_business_id()
        toggle_bookmark(user_id, business_id)
        if self.ui.bookmark_button.isChecked():
            self.ui.bookmark_button.setIcon(self.filled_icon)
        else:
            self.ui.bookmark_button.setIcon(self.unfilled_icon)

        app_session.update_user_bookmarks()

