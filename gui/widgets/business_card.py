from PySide6.QtWidgets import QFrame
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QMouseEvent, QPixmap, QIcon

from services import BusinessData
import services

from gui.generated.ui_business_card import Ui_Form as business_card

# Class for the business cards that populate discover page
class BusinessCard(QFrame):
    # create a click signal to notify when this card is clicked, passing the business object
    clicked = Signal(object)

    def __init__(self, business: BusinessData): #Business object that is represented by this card
        # Initialize widget and load layout from its .ui file
        super().__init__()
        self.ui = business_card()
        self.ui.setupUi(self)
        
        # Set info/text
        self.business = business

        self.id = business.id

        self.ui.title.setText(business.name)
        self.ui.category.setText(business.category)
        self.ui.ratings.setText(business.rating_str)

        self.unfilled_icon = QIcon("images/icons/yellow_unfilled_bookmark.png")
        self.filled_icon = QIcon("images/icons/yellow_filled_bookmark.png")

        self.ui.bookmark_button.clicked.connect(self.toggle_bookmark)

        if business.bookmarked:
            self.ui.bookmark_button.setIcon(self.filled_icon)
            self.ui.bookmark_button.setChecked(True)
        else:
            self.ui.bookmark_button.setIcon(self.unfilled_icon)


        # Load image and crop square from center
        pixmap = QPixmap(business.thumbnail_link)
        # square = None
        # Ensure pixmap loaded
        # if not pixmap.isNull():
        #     # choose smaller length as size
        #     size = min(pixmap.width(), pixmap.height())
            
        #     # Calculate center point
        #     x = (pixmap.width() - size) // 2
        #     y = (pixmap.height() - size) // 2

        #     # Crop original based on center point
        #     square = pixmap.copy(x, y, size, size)

        #     square = square.scaled(
        #         self.ui.thumbnail.width(),
        #         self.ui.thumbnail.height(),
        #         Qt.AspectRatioMode.KeepAspectRatioByExpanding,
        #         Qt.TransformationMode.SmoothTransformation
        #     )
        # if square is not None:
        self.ui.thumbnail.setPixmap(pixmap)

        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.clicked.emit(self.business)
        return super().mousePressEvent(event)
    
    def keyPressEvent(self, event):
        if event.key() in (Qt.Key.Key_Space, Qt.Key.Key_Enter, Qt.Key.Key_Return):
            self.clicked.emit(self.business)
            event.accept()
            return 
        super().keyPressEvent(event)


    def toggle_bookmark(self):
        user_id = services.app_session.get_user_id()
        services.toggle_bookmark(user_id, self.id)

        if self.ui.bookmark_button.isChecked():
            self.ui.bookmark_button.setIcon(self.filled_icon)
        else:
            self.ui.bookmark_button.setIcon(self.unfilled_icon)
