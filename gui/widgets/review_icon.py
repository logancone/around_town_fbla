from PySide6.QtWidgets import QFrame

from database import Review
import services

from gui.generated.ui_review_icon import Ui_Form as review_icon

# Class for the review icons that populate business page
class ReviewIcon(QFrame):
    def __init__(self, review: Review):
        # Init class and load .ui
        super().__init__()

        self.ui = review_icon()
        self.ui.setupUi(self)
        self.setObjectName(u"ReviewIcon")

        # Set size
        self.setFixedSize(800, 100)

        # Set info/text
        header_text = f"{services.get_username_from_id(review.user_id)}: ⭐{review.rating}"
        self.ui.header.setText(header_text)
        self.ui.body.setText(review.content)
