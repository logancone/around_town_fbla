from PySide6.QtWidgets import QFrame
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QMouseEvent, QPixmap, QIcon, QFont

from database import Business
from services.user_services import toggle_bookmark
from app_session import app_session

from gui.generated.ui_business_card import Ui_Form as business_card

# Class for the business cards that populate discover page and profile page, contains:
# Title, category, rating, and thumbnail
class BusinessCard(QFrame):
    # create a click signal to notify when this card is clicked, passing the business object
    clicked = Signal(object)

    # Initialize class and setup ui
    def __init__(self, business: Business): #Business object that is represented by this card
        super().__init__()
        self.ui = business_card()
        self.ui.setupUi(self)
        
        # Set info/text
        self.business = business

        self.id = business.id

        self.ui.title.setText(business.name)
        # Dynamically adjust title fit:
        if len(business.name) >= 23:
            # self.ui.title.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
            self.ui.title.setStyleSheet("font-size: 12.95px;")
        self.ui.title.adjustSize()
        self.ui.category.setText(business.category.capitalize())

        # Create and set rating string
        if business.rating_count > 0:
            self.ui.ratings.setText(f"⭐{business.avg_rating} ({business.rating_count})")
        else:
            self.ui.ratings.setText("No reviews")

        # Load the bookmark icons
        self.unfilled_icon = QIcon("resources/images/icons/yellow_unfilled_bookmark.png")
        self.filled_icon = QIcon("resources/images/icons/yellow_filled_bookmark.png")

        self.ui.bookmark_button.clicked.connect(self.bookmark_toggle)

        # Determine if the business is bookmarked for the current active user, and set bookmark state accordingly
        if app_session.is_business_bookmarked(business.id):
            self.ui.bookmark_button.setIcon(self.filled_icon)
            self.ui.bookmark_button.setChecked(True)
        else:
            self.ui.bookmark_button.setIcon(self.unfilled_icon)

        # Load thumbnail
        pixmap = QPixmap(business.thumbnail_link)
        # scaled_pixmap = pixmap.scaled(self.ui.thumbnail.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        
        self.ui.thumbnail.setPixmap(pixmap)

        # Allow card to be focused from mouse click and key click
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.setAccessibleName(f"Business Card for {business.name}")

    # Runs when the mouse clicks the business card, emits the clicked signal containing its business info
    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.clicked.emit(self.business)
        return super().mousePressEvent(event)
    
    # Runs when either the spacebar or enter/return key is pressed while the card is focused, allows cards to be selected via keyboard
    def keyPressEvent(self, event):
        if event.key() in (Qt.Key.Key_Space, Qt.Key.Key_Enter, Qt.Key.Key_Return):
            self.clicked.emit(self.business)
            event.accept()
            return 
        super().keyPressEvent(event)

    # Toggles the bookmarked state of the business for the current user, and updates the icon
    def bookmark_toggle(self):
        user_id = app_session.user_id
        toggle_bookmark(user_id, self.id)

        if self.ui.bookmark_button.isChecked():
            self.ui.bookmark_button.setIcon(self.filled_icon)
        else:
            self.ui.bookmark_button.setIcon(self.unfilled_icon)
        
        app_session.update_user_bookmarks()
