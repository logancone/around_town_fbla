from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QSize, Signal
from PySide6.QtGui import QIcon

from database import Business
import services

from gui.generated.ui_business_page import Ui_Form as business_page

from gui.widgets.review_icon import ReviewIcon
from gui.widgets.review_editor import ReviewEditor

class BusinessPage(QWidget):
    return_pressed = Signal()

    def __init__(self):
        # Init class and load ui
        super().__init__()
        self.ui = business_page()
        self.ui.setupUi(self)

        self.review_list: list[ReviewIcon] = []

        self.unfilled_icon = QIcon("images/icons/yellow_unfilled_bookmark.png")
        self.filled_icon = QIcon("images/icons/yellow_filled_bookmark.png")

        self.ui.bookmark_button.setIconSize(QSize(32, 32))

        self.ui.add_review_button.clicked.connect(self.open_review_editor)
        self.ui.bookmark_button.clicked.connect(self.toggle_bookmark)
        self.ui.back_button.clicked.connect(self.return_to_discover_page)

    def set_to_business(self, business: Business):
        # self.clear_reviews()
        self.ui.business_page_title.setText(business.name)
        self.ui.description.setText(business.business_description)
        
        tags = services.get_tags_from_business(business.id)
        tag_str = f"Tags: {tags.pop(0)}"
        for tag in tags:
            tag_str += f", {tag}"
        self.ui.tag_label.setText(tag_str)


        if services.check_if_bookmark(services.app_session.user_id, services.app_session.business_id):
            self.ui.bookmark_button.setIcon(self.filled_icon)
            self.ui.bookmark_button.setChecked(True)
        else:
            self.ui.bookmark_button.setIcon(self.unfilled_icon)

        self.load_reviews()
        # reviews = services.get_reviews(business.id)

        # for review in reviews:
        #     review_icon = ReviewIcon(review)
        #     # card.clicked.connect()
        #     self.ui.review_holder.addWidget(review_icon)
        #     self.review_list.append(review_icon)
        #     # self.review_holder.append(card)

    def load_reviews(self):
        self.clear_reviews()
        reviews = services.get_reviews(services.app_session.get_business_id())

        for review in reviews:
            review_icon = ReviewIcon(review)
            # card.clicked.connect()
            self.ui.review_holder.addWidget(review_icon)
            self.review_list.append(review_icon)
            # self.review_holder.append(card)

    def clear_reviews(self):
        for review in self.review_list:
            review.deleteLater()
        
        self.review_list.clear()
    
    def open_review_editor(self):
        editor = ReviewEditor()
        editor.accepted.connect(self.load_reviews)
        editor.exec()

    def toggle_bookmark(self):
        user_id = services.app_session.get_user_id()
        business_id = services.app_session.get_business_id()
        services.toggle_bookmark(user_id, business_id)
        if self.ui.bookmark_button.isChecked():
            self.ui.bookmark_button.setIcon(self.filled_icon)
        else:
            self.ui.bookmark_button.setIcon(self.unfilled_icon)

    def return_to_discover_page(self):
        self.return_pressed.emit()
