from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

import services

from gui.generated.ui_login_page import Ui_Form as login_page

class LoginPage(QWidget):
    login_success = Signal()
    signup_request = Signal()

    def __init__(self):
        super().__init__()
        self.ui = login_page()
        self.ui.setupUi(self)

        self.ui.login_button.clicked.connect(self.attempt_login)
        self.ui.signup_button.clicked.connect(self.signup_request.emit)

    # Return True if username and password are valid inputs, else return false
    def validate_login_input(self, username, password):
        # Ensure both fields have text
        if len(username) == 0 or len(password) == 0:
            self.ui.error_label.setText("Please fill out all fields!")
            return False

        return True
    
    def attempt_login(self):
        username = self.ui.username_entry.text()
        password = self.ui.password_entry.text()
        # If both fields have valid inputs
        if self.validate_login_input(username, password) == True:
            user = services.authenticate_user(username, password)

            if user is None:
                self.ui.error_label.setText("Invalid username or password!")
            else:
                self.ui.error_label.setText("Success!")
                services.app_session.set_user_id(user.id)
                self.login_success.emit()
    
    def clear_text(self):
        self.ui.username_entry.setText('')
        self.ui.password_entry.setText('')
        self.ui.error_label.setText('')
