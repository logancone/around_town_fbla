from PySide6.QtWidgets import QMainWindow

from gui.generated.ui_main_window import Ui_MainWindow as main_window

from gui.pages.login_page import LoginPage
from gui.pages.signup_page import SignupPage
from gui.shell.nav_shell import NavShell

# Represents the main window of the application, which houses everything else. 
# Directly, this window can switch between the login page, signup page, and navshell, which contains the rest of the program
class MainWindow(QMainWindow):
    # Initalize class and setup ui
    def __init__(self):
        super().__init__()
        self.ui = main_window()
        self.ui.setupUi(self)

        # Establish pages and add them to the stacked widget
        self.login_page = LoginPage()
        self.signup_page = SignupPage()
        self.nav_shell = NavShell()
        
        self.ui.outer_stack.addWidget(self.login_page)
        self.ui.outer_stack.addWidget(self.signup_page)
        self.ui.outer_stack.addWidget(self.nav_shell)

        # Set the starting widget to the login page
        self.ui.outer_stack.setCurrentWidget(self.login_page)

        # Connect page signals to appropriate actions
        self.login_page.login_success.connect(self.set_nav_shell)
        self.login_page.signup_request.connect(self.set_signup_page)
        self.signup_page.signup_success.connect(self.set_nav_shell)
        self.signup_page.login_request.connect(self.set_login_page)

        self.nav_shell.logout.connect(self.set_login_page)

    # Sets current page to the login page
    def set_login_page(self):
        self.ui.outer_stack.setCurrentWidget(self.login_page)
    
    # Sets current page to the signup page
    def set_signup_page(self):
        self.ui.outer_stack.setCurrentWidget(self.signup_page)

    # Sets current page to navshell, sets navshell to the discover page, and clears inputs from login and signup pages
    def set_nav_shell(self):
        self.nav_shell.set_discover_page()
        self.ui.outer_stack.setCurrentWidget(self.nav_shell)
        self.login_page.clear_text()
        self.signup_page.clear_text()
