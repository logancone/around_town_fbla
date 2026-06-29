from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

from services.user_services import (
    get_username_from_id, 
    generate_user_report
)

from services.business_services import get_business_from_id

from gui.generated.ui_profile_page import Ui_Form as profile_page

from gui.widgets.business_card import BusinessCard
from gui.widgets.report_editor import ReportEditor
from gui.widgets.location_editor import LocationEditor

from app_session import app_session

# Represents the profile page, contains user data such as bookmarked businesses, as well as the ability to download user report
class ProfilePage(QWidget):
    # Signal to be sent to the navshell if the user clicks a business card from the bookmarks section
    business_selected = Signal(object)

    # Initialize class and setup ui
    def __init__(self):
        super().__init__()
        self.ui = profile_page()
        self.ui.setupUi(self)
        self.cur_user_id = -1

        # List of the bookmarked business cards for easy cleanup
        self.bookmark_list: list[BusinessCard] = []

        self.ui.report_gen_button.clicked.connect(self.open_report_editor)
        self.ui.settings_button.clicked.connect(self.open_location_editor)

    # Clears all the cards by iterating through bookmark list
    def clear_bookmarks(self):
        for card in self.bookmark_list:
            card.deleteLater()
        self.bookmark_list.clear()

    # Loads user information from db and displays on the page
    def load_profile(self, user_id):
        self.cur_user_id = user_id
        self.clear_bookmarks()
        username = get_username_from_id(user_id)

        if username is not None:
            self.ui.username_label.setText(username)

            # Go through all bookmarked businesses and create a card
            bookmarks = app_session.users_bookmarks
            for bookmark in bookmarks:
                business = get_business_from_id(bookmark)
                assert business

                card = BusinessCard(business)
                card.clicked.connect(self.card_clicked)
                self.ui.horizontalLayout_2.addWidget(card)
                self.bookmark_list.append(card)
    
    # Creates a pop-up for the user to edit report information
    def open_report_editor(self):
        editor = ReportEditor()
        editor.exec()

    # Creates a pop-up for the user to edit location information
    def open_location_editor(self):
        editor = LocationEditor()
        editor.exec()
    
    # Emit the signal if the user presses a business card
    def card_clicked(self, business):
        self.business_selected.emit(business)

