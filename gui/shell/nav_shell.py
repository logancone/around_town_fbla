from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

from app_session import app_session

from gui.generated.ui_nav_shell import Ui_Form as nav_shell

from gui.pages.discover_page import DiscoverPage
from gui.pages.business_page import BusinessPage
from gui.pages.profile_page import ProfilePage
    
class NavShell(QWidget):
    logout = Signal()
    def __init__(self):
        super().__init__()
        self.ui = nav_shell()
        self.ui.setupUi(self)

        self.ui.profile_button.clicked.connect(self.set_profile_page)
        self.ui.discover_button.clicked.connect(self.set_discover_page)
        self.ui.logout_button.clicked.connect(self.logout_pressed)

        # Establish pages
        self.discover_page = DiscoverPage()
        self.business_page = BusinessPage()
        self.profile_page = ProfilePage()

        self.ui.page_stack.addWidget(self.discover_page)
        self.ui.page_stack.addWidget(self.business_page)
        self.ui.page_stack.addWidget(self.profile_page)

        self.set_discover_page()

        self.discover_page.business_selected.connect(self.set_business_page)
        self.profile_page.business_selected.connect(self.set_business_page)

        self.business_page.return_pressed.connect(self.set_discover_page)

        user_id = app_session.get_user_id()
        self.profile_page.load_profile(user_id)
        
    def set_discover_page(self):
        app_session.leave_business()
        self.discover_page.load_all_business_data()
        self.discover_page.populate_cards(self.discover_page.all_business_data)
        self.ui.page_stack.setCurrentWidget(self.discover_page)

    def set_business_page(self, business):
        app_session.set_business_id(business.id)
        self.business_page.set_to_business(business)
        self.ui.page_stack.setCurrentWidget(self.business_page)

    def set_profile_page(self):
        self.profile_page.load_profile(app_session.get_user_id())
        self.ui.page_stack.setCurrentWidget(self.profile_page)

    def logout_pressed(self):
        app_session.logout_user()
        self.logout.emit()

    # def user_logged_in(self):
    #     user_id = services.app_session.get_user_id()
    #     self.profile_page.load_profile(user_id)
