from PySide6.QtWidgets import QDialog

from services.business_services import add_review
from app_session import app_session

from gui.generated.ui_review_editor import Ui_Dialog as review_editor

# Represents the dialog popup that allows users to give businesses ratings and write reviews
class ReviewEditor(QDialog):
    # Initialize class and setup ui
    def __init__(self):
        super().__init__()
        self.ui = review_editor()
        self.ui.setupUi(self)
        
        # Rating bar runs from 0-10 (to allow for .5s) so set the text to the value of the rating bar / 2
        self.ui.rating_label.setText(f"{self.ui.rating_bar.value() / 2} ⭐")
        self.ui.rating_bar.valueChanged.connect(self.update_rating_text)

        # Send the review to the database when user pressed accept button
        self.accepted.connect(self.send_review)

    # Sets the text of the rating bar to half the rating bar's value, since rating bar runs from 0-10 but rating is from 0-5
    def update_rating_text(self):
        self.ui.rating_label.setText(f"{self.ui.rating_bar.value() / 2} ⭐")
    
    # Adds the review to the database using currently selected user id and business id along with the entered information
    def send_review(self):
        user_id = app_session.get_user_id()
        business_id = app_session.get_business_id()
        rating = self.ui.rating_bar.value() / 2
        content = self.ui.review_content.toPlainText()
        
        add_review(user_id, business_id, rating, content)
