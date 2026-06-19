from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

from services.user_services import authenticate_user
from app_session import app_session

from gui.generated.ui_login_page import Ui_Form as login_page

# Represents the login page for the application, just has username and password inputs
class LoginPage(QWidget):
    # Signals to be sent to the main window if the user successfully logs in or switches to the signup page
    login_success = Signal()
    signup_request = Signal()

    # Initialize class and setup ui
    def __init__(self):
        super().__init__()
        self.ui = login_page()
        self.ui.setupUi(self)

        self.ui.login_button.clicked.connect(self.attempt_login)
        self.ui.signup_button.clicked.connect(self.signup_request.emit)

    # Return True if username and password are valid inputs (at least 1 character), else return false
    def validate_login_input(self, username, password):
        # Ensure both fields have text
        if len(username) == 0 or len(password) == 0:
            self.ui.error_label.setText("Please fill out all fields!")
            return False
        return True
    
    # Read the current input for username and password and attempt to login by checking the database
    def attempt_login(self):
        username = self.ui.username_entry.text()
        password = self.ui.password_entry.text()

        # Ensure both fields have valid inputs
        if self.validate_login_input(username, password) == True:
            user = authenticate_user(username, password)

            # Check if the user actually exists, if so, run login logic
            if user is None:
                self.ui.error_label.setText("Invalid username or password!")
            else:
                self.ui.error_label.setText("Success!")
                app_session.set_user_id(user.id)
                self.login_success.emit()
    
    # Sets all text fields to empty
    def clear_text(self):
        self.ui.username_entry.setText('')
        self.ui.password_entry.setText('')
        self.ui.error_label.setText('')
