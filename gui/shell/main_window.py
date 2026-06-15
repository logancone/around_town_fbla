from PySide6.QtWidgets import QMainWindow

from gui.generated.ui_main_window import Ui_MainWindow as main_window

from gui.pages.login_page import LoginPage
from gui.pages.signup_page import SignupPage
from gui.shell.nav_shell import NavShell

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = main_window()
        self.ui.setupUi(self)

        # Establish pages
        self.login_page = LoginPage()
        self.signup_page = SignupPage()
        self.nav_shell = NavShell()
        
        self.ui.outer_stack.addWidget(self.login_page)
        self.ui.outer_stack.addWidget(self.signup_page)
        self.ui.outer_stack.addWidget(self.nav_shell)

        self.ui.outer_stack.setCurrentWidget(self.login_page)
        # self.ui.outer_stack.setCurrentWidget(self.nav_shell)

        self.login_page.login_success.connect(self.set_nav_shell)
        self.login_page.signup_request.connect(self.set_signup_page)
        self.signup_page.signup_success.connect(self.set_nav_shell)
        self.signup_page.login_request.connect(self.set_login_page)

        self.nav_shell.logout.connect(self.set_login_page)

    def set_login_page(self):
        self.ui.outer_stack.setCurrentWidget(self.login_page)
    
    def set_signup_page(self):
        self.ui.outer_stack.setCurrentWidget(self.signup_page)

    def set_nav_shell(self):
        # self.nav_shell.user_logged_in()
        self.nav_shell.set_discover_page()
        self.ui.outer_stack.setCurrentWidget(self.nav_shell)
        self.login_page.clear_text()
        self.signup_page.clear_text()
