from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

from app_session import app_session

from gui.generated.ui_nav_shell import Ui_Form as nav_shell

from gui.pages.discover_page import DiscoverPage
from gui.pages.business_page import BusinessPage
from gui.pages.profile_page import ProfilePage
    
# Represents the navshell, whcih houses the profile page and discover page, along with the navbar to navigate between them
class NavShell(QWidget):
    # Signal that tells the main window to switch to the log out page
    logout = Signal()

    # Initialize class and setup ui
    def __init__(self):
        super().__init__()
        self.ui = nav_shell()
        self.ui.setupUi(self)

        # Connect button logic
        self.ui.profile_button.clicked.connect(self.set_profile_page)
        self.ui.discover_button.clicked.connect(self.set_discover_page)
        self.ui.logout_button.clicked.connect(self.logout_pressed)

        # Establish pages
        self.discover_page = DiscoverPage()
        self.business_page = BusinessPage()
        self.profile_page = ProfilePage()

        # Add pages to the stack and set the current page
        self.ui.page_stack.addWidget(self.discover_page)
        self.ui.page_stack.addWidget(self.business_page)
        self.ui.page_stack.addWidget(self.profile_page)

        self.discover_page.load_all_business_data()

        self.set_discover_page()

        self.discover_page.business_selected.connect(self.set_business_page)
        self.profile_page.business_selected.connect(self.set_business_page)

        self.business_page.return_pressed.connect(self.set_discover_page)

        user_id = app_session.user_id
        self.profile_page.load_profile(user_id)

        
    
    # Sets current page to the discover page, along with loading all cards.
    def set_discover_page(self):
        app_session.leave_business()
        # Refresh discover cards so bookmark state stays in sync after changes.
        self.discover_page.refresh_cards()
        self.ui.page_stack.setCurrentWidget(self.discover_page)

    # Sets current page to the business page, loading all business info
    def set_business_page(self, business):
        app_session.set_business_id(business.id)
        self.business_page.set_to_business(business)
        self.ui.page_stack.setCurrentWidget(self.business_page)

    # Sets current page to the profile page, loading all profile info
    def set_profile_page(self):
        self.profile_page.load_profile(app_session.user_id)
        self.ui.page_stack.setCurrentWidget(self.profile_page)

    # Logs out the user and emits logout signal
    def logout_pressed(self):
        app_session.logout_user()
        self.logout.emit()
