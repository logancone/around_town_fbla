from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal
from PySide6.QtGui import QPixmap, QIcon

from services.user_services import add_user, is_username_available
from app_session import app_session
import random

from gui.generated.ui_signup_page import Ui_Form as signup_page

import pyttsx3

# Represents the signup page, where users can create new accounts by entering username, password, and completing a captcha
class SignupPage(QWidget):
    # Signals to be sent to main window if the user sucessfully signs up or switches to login page
    signup_success = Signal()
    login_request = Signal()

    # Initialize class and setup ui
    def __init__(self):
        super().__init__()
        self.ui = signup_page()
        self.ui.setupUi(self)
        
        # Load CAPTCHAS
        self.captchas = [
            '2g7nm',
            '7pn5g',
            '8y6b3',
            '32dnn',
            '42dw4',
            'c2fb7',
            'excmn',
            'gfp54',
            'mg5nn',
            'x8xnp'
        ]
        self.load_random_captcha()

        # Initialize text-to-speech engine for audio captchas
        # self.tts_engine = pyttsx3.init()

        # Link to the play and playing icons, and set button to 'play'
        self.play_icon = QIcon("resources/images/icons/play_button.png")
        self.sound_playing_icon = QIcon("resources/images/icons/sound_playing.png")

        self.ui.audio_play_button.setIcon(self.play_icon)
        
        # Connect buttons to functions
        self.ui.signup_button.clicked.connect(self.attempt_signup)
        self.ui.login_button.clicked.connect(self.login_request.emit)
        self.ui.reload_button.clicked.connect(self.load_random_captcha)
        self.ui.audio_play_button.clicked.connect(self.speak_current_captcha)

        

    # Return True if username and password are valid inputs, else return false
    def validate_signup_input(self, username, password, confirm_password, captcha_attempt):
        # Ensure both fields have text
        if len(username) == 0 or len(password) == 0:
            self.ui.error_label.setText("Please fill out all fields!")
            return False

        # Ensure username is between 4-25 characters
        if len(username) < 4 or len(username) > 25:
            self.ui.error_label.setText("Ensure username is between 4-25 characters!")
            return False
        
        # Ensure password is between 4-35 characters
        if len(username) < 4 or len(username) > 35:
            self.ui.error_label.setText("Ensure password is between 4-35 characters!")
            return False
        
        # Ensure password and confirm password match
        if password != confirm_password:
            self.ui.error_label.setText("Both passwords must match!")
            return False
        
        # Ensure username is unique
        if is_username_available(username) == False:
            self.ui.error_label.setText("Username is already taken!")
            return False
        
        # Ensure captcha is correct
        if captcha_attempt != self.cur_captcha:
            self.ui.error_label.setText("Incorrect CAPTCHA!")
            return False
        
        return True
    
    # Take in all the info from the page, check it all, and if it is valid create a new account
    def attempt_signup(self):
        username = self.ui.username_entry.text()
        password = self.ui.password_entry.text()
        confirm_password = self.ui.confirm_password_entry.text()
        captcha_attempt = self.ui.captcha_entry.text().lower()

        # If both fields have valid inputs, add new account to the database
        if self.validate_signup_input(username, password, confirm_password, captcha_attempt) == True:
            new_user_id = add_user(username, password)
            self.ui.error_label.setText("Success!")
            app_session.set_user_id(new_user_id)
            self.signup_success.emit()

    # Choose a random captcha from the list, and display the matching image
    def load_random_captcha(self):
        num = random.randint(0, len(self.captchas)-1)
        self.cur_captcha = self.captchas[num]

        captcha_path = f'resources/images/captchas/{self.cur_captcha}.png'
        self.ui.captcha_display.setPixmap(QPixmap(captcha_path))

    # Use the text-to-speech engine to say the current captcha aloud, and change button state for user feedback
    def speak_current_captcha(self):
        spoken_str = ""
        for letter in self.cur_captcha:
            spoken_str += f"{letter} "

        self.ui.audio_play_button.setIcon(self.sound_playing_icon)
        self.ui.audio_play_button.setDisabled(True)

        engine = pyttsx3.init()
        engine.say(" ".join(self.cur_captcha.upper()))
        engine.runAndWait()

        self.ui.audio_play_button.setIcon(self.play_icon)
        self.ui.audio_play_button.setDisabled(False)

    # Set all text fields to empty
    def clear_text(self):
        self.ui.username_entry.setText('')
        self.ui.password_entry.setText('')
        self.ui.confirm_password_entry.setText('')
        self.ui.captcha_entry.setText('')
        self.ui.error_label.setText('')
