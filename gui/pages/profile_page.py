from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

import services

from gui.generated.ui_profile_page import Ui_Form as profile_page

from gui.widgets.business_card import BusinessCard

class ProfilePage(QWidget):
    business_selected = Signal(object)
    def __init__(self):
        super().__init__()
        self.ui = profile_page()
        self.ui.setupUi(self)
        self.bookmark_list: list[BusinessCard] = []

        self.ui.report_gen_button.clicked.connect(services.generate_user_report)


    def load_profile(self, user_id):
        self.clear_bookmarks()
        username = services.get_username_from_id(user_id)
        if username is not None:
            self.ui.username_label.setText(username)

            bookmarks = services.get_bookmarks_by_user(user_id)
            for bookmark in bookmarks:
                business = services.get_business_data_from_id(bookmark.business_id)
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
