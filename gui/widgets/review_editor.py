from PySide6.QtWidgets import QDialog

from services.business_services import add_review
from app_session import app_session

from gui.generated.ui_review_editor import Ui_Dialog as review_editor

class ReviewEditor(QDialog):
    def __init__(self): #
        # Initialize widget and load layout from its .ui file
        super().__init__()
        self.ui = review_editor()
        self.ui.setupUi(self)

        self.ui.rating_label.setText(f"{self.ui.rating_bar.value() / 2} ⭐")
        self.ui.rating_bar.valueChanged.connect(self.update_rating_text)
        self.accepted.connect(self.send_review)

    def update_rating_text(self):
        self.ui.rating_label.setText(f"{self.ui.rating_bar.value() / 2} ⭐")
        
    def send_review(self):
        user_id = app_session.get_user_id()
        business_id = app_session.get_business_id()
        rating = self.ui.rating_bar.value() / 2
        content = self.ui.review_content.toPlainText()
        
        add_review(user_id, business_id, rating, content)
