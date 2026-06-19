from PySide6.QtWidgets import QFrame

from database import Review
from services.user_services import get_username_from_id

from gui.generated.ui_review_icon import Ui_Form as review_icon

# Class for the review icons that populate business page, contains reviewer name, rating, and review content
class ReviewIcon(QFrame):
    def __init__(self, review: Review):
        # Initialize class and setup ui
        super().__init__()

        self.ui = review_icon()
        self.ui.setupUi(self)
        
        # Sets the object to the correct name
        self.setObjectName(u"ReviewIcon")

        # Set fixed size
        self.setFixedSize(800, 100)

        # Set info/text
        header_text = f"{get_username_from_id(review.user_id)}: ⭐{review.rating}"
        self.ui.header.setText(header_text)
        self.ui.body.setText(review.content)
