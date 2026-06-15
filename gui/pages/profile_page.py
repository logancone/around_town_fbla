from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

from services.user_services import (
    get_username_from_id, 
    generate_user_report
)

from services.business_services import get_business_from_id

from gui.generated.ui_profile_page import Ui_Form as profile_page

from gui.widgets.business_card import BusinessCard

from app_session import app_session

class ProfilePage(QWidget):
    business_selected = Signal(object)
    def __init__(self):
        super().__init__()
        self.ui = profile_page()
        self.ui.setupUi(self)
        self.bookmark_list: list[BusinessCard] = []

        self.ui.report_gen_button.clicked.connect(generate_user_report)


    def load_profile(self, user_id):
        self.clear_bookmarks()
        username = get_username_from_id(user_id)
        if username is not None:
            self.ui.username_label.setText(username)

            bookmarks = app_session.get_user_bookmarks()
            for bookmark in bookmarks:
                business = get_business_from_id(bookmark)
                assert business

                card = BusinessCard(business)
                card.clicked.connect(self.card_clicked)
                self.ui.horizontalLayout_2.addWidget(card)
                self.bookmark_list.append(card)

    def clear_bookmarks(self):
        for card in self.bookmark_list:
            card.deleteLater()
        self.bookmark_list.clear()

    def card_clicked(self, business):
        self.business_selected.emit(business)
