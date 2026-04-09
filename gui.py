from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel, QGridLayout, QSizePolicy, QMainWindow, QStackedWidget, QFrame, QTextEdit, QVBoxLayout, QScrollArea, QDialog
from PySide6.QtCore import QFile, QSize, Signal, Qt
from PySide6.QtGui import QMouseEvent, QPixmap, QIcon

from database import Business, Review
import services

from ui.main_window import Ui_MainWindow as main_window
from ui.nav_shell import Ui_Form as nav_shell
from ui.login_page import Ui_Form as login_page
from ui.signup_page import Ui_Form as signup_page
from ui.business_card import Ui_Form as business_card
from ui.discover_page import Ui_Form as discover_page
from ui.review_icon import Ui_Form as review_icon
from ui.business_page import Ui_Form as business_page
from ui.review_editor import Ui_Dialog as review_editor
from ui.profile_page import Ui_Form as profile_page

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
        self.ui.outer_stack.setCurrentWidget(self.nav_shell)
    
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

        self.discover_page.populate_cards(services.get_businesses_all())
        self.ui.page_stack.setCurrentWidget(self.discover_page)

        self.discover_page.business_selected.connect(self.set_business_page)
        self.profile_page.business_selected.connect(self.set_business_page)

        user_id = services.app_session.get_user_id()
        self.profile_page.load_profile(user_id)
        
    def set_discover_page(self):
        services.app_session.leave_business()
        self.discover_page.populate_cards(services.get_businesses_all())
        self.ui.page_stack.setCurrentWidget(self.discover_page)

    def set_business_page(self, business):
        services.app_session.set_business_id(business.id)
        self.business_page.set_to_business(business)
        self.ui.page_stack.setCurrentWidget(self.business_page)

    def set_profile_page(self):
        self.profile_page.load_profile(services.app_session.get_user_id())
        self.ui.page_stack.setCurrentWidget(self.profile_page)

    def logout_pressed(self):
        self.set_discover_page()
        services.app_session.logout_user()
        self.logout.emit()

    # def user_logged_in(self):
    #     user_id = services.app_session.get_user_id()
    #     self.profile_page.load_profile(user_id)

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

class SignupPage(QWidget):
    signup_success = Signal()
    login_request = Signal()

    def __init__(self):
        super().__init__()
        self.ui = signup_page()
        self.ui.setupUi(self)

        self.ui.signup_button.clicked.connect(self.attempt_signup)
        self.ui.login_button.clicked.connect(self.login_request.emit)

    # Return True if username and password are valid inputs, else return false
    def validate_signup_input(self, username, password, confirm_password):
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
        if services.is_username_available(username) == False:
            self.ui.error_label.setText("Username is already taken!")
            return False
        
        return True
    
    def attempt_signup(self):
        username = self.ui.username_entry.text()
        password = self.ui.password_entry.text()
        confirm_password = self.ui.confirm_password_entry.text()

        # If both fields have valid inputs
        if self.validate_signup_input(username, password, confirm_password) == True:
            new_user_id = services.add_user(username, password)
            self.ui.error_label.setText("Success!")
            services.app_session.set_user_id(new_user_id)
            self.signup_success.emit()

# Class for the business cards that populate discover page
class BusinessCard(QFrame):
    # create a click signal to notify when this card is clicked, passing the business object
    clicked = Signal(object)

    def __init__(self, business: Business): #Business object that is represented by this card
        # Initialize widget and load layout from its .ui file
        super().__init__()
        self.ui = business_card()
        self.ui.setupUi(self)
        
        # Set info/text
        self.business = business

        self.id = business.id

        self.ui.title.setText(business.name)
        self.ui.category.setText(business.category)
        self.ui.ratings.setText(services.get_rating_str(business.id))

        self.unfilled_icon = QIcon("images/icons/unfilled_bookmark.png")
        self.filled_icon = QIcon("images/icons/filled_bookmark.png")

        self.ui.bookmark_button.clicked.connect(self.toggle_bookmark)

        if services.check_if_bookmark(services.app_session.user_id, self.id):
            self.ui.bookmark_button.setIcon(self.filled_icon)
            self.ui.bookmark_button.setChecked(True)
        else:
            self.ui.bookmark_button.setIcon(self.unfilled_icon)


        # Load image and crop square from center
        pixmap = QPixmap(business.thumbnail_link)
        square = None
        # Ensure pixmap loaded
        if not pixmap.isNull():
            # choose smaller length as size
            size = min(pixmap.width(), pixmap.height())
            
            # Calculate center point
            x = (pixmap.width() - size) // 2
            y = (pixmap.height() - size) // 2

            # Crop original based on center point
            square = pixmap.copy(x, y, size, size)

            square = square.scaled(
                self.ui.thumbnail.width(),
                self.ui.thumbnail.height(),
                Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                Qt.TransformationMode.SmoothTransformation
            )
        if square is not None:
            self.ui.thumbnail.setPixmap(square)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.clicked.emit(self.business)
        return super().mousePressEvent(event)
    
    def toggle_bookmark(self):
        user_id = services.app_session.get_user_id()
        services.toggle_bookmark(user_id, self.id)

        if self.ui.bookmark_button.isChecked():
            self.ui.bookmark_button.setIcon(self.filled_icon)
        else:
            self.ui.bookmark_button.setIcon(self.unfilled_icon)

# Class for the discover page
class DiscoverPage(QWidget):
    business_selected = Signal(object)

    def __init__(self):
        # Init class and load ui
        super().__init__()
        self.ui = discover_page()
        self.ui.setupUi(self)

        self.card_list : list[BusinessCard] = []

        self.ui.retail_button.clicked.connect(lambda: self.filter_cards_by_category("Retail"))
        self.ui.food_button.clicked.connect(lambda: self.filter_cards_by_category("Food"))
        self.ui.entertainment_button.clicked.connect(lambda: self.filter_cards_by_category("Entertainment"))
        self.ui.services_button.clicked.connect(lambda: self.filter_cards_by_category("Services"))

        self.ui.ratings_descending_button.clicked.connect(lambda: self.sort_cards_by_rating(False))
        self.ui.ratings_ascending_button.clicked.connect(lambda: self.sort_cards_by_rating(True))
        

    def populate_cards(self, businesses):
        self.clear_cards()

        for i, business in enumerate(businesses):
            card = BusinessCard(business)
            card.clicked.connect(self.card_clicked)
            self.ui.grid_layout.addWidget(card, i//3, i%3)
            self.card_list.append(card)

    def clear_cards(self):
        for card in self.card_list:
            card.deleteLater()
        self.card_list.clear()

    def filter_cards_by_category(self, category):
        self.populate_cards(services.get_businesses_by_category(category))
    
    def sort_cards_by_rating(self, ascending):
        self.populate_cards(services.sort_businesses_by_rating(ascending))

    def card_clicked(self, business):
        self.business_selected.emit(business)

# Class for the review icons that populate business page
class ReviewIcon(QFrame):
    def __init__(self, review: Review):
        # Init class and load .ui
        super().__init__()

        self.ui = review_icon()
        self.ui.setupUi(self)
        self.setObjectName(u"ReviewIcon")

        # Set size
        self.setFixedSize(800, 100)

        # Set info/text
        header_text = f"{services.get_username_from_id(review.user_id)}: ⭐{review.rating}"
        self.ui.header.setText(header_text)
        self.ui.body.setText(review.content)

class BusinessPage(QWidget):
    def __init__(self):
        # Init class and load ui
        super().__init__()
        self.ui = business_page()
        self.ui.setupUi(self)

        self.review_list: list[ReviewIcon] = []

        self.unfilled_icon = QIcon("images/icons/unfilled_bookmark.png")
        self.filled_icon = QIcon("images/icons/filled_bookmark.png")

        self.ui.bookmark_button.setIconSize(QSize(32, 32))

        self.ui.add_review_button.clicked.connect(self.open_review_editor)
        self.ui.bookmark_button.clicked.connect(self.toggle_bookmark)

    def set_to_business(self, business: Business):
        # self.clear_reviews()
        self.ui.business_page_title.setText(business.name)
        self.ui.description.setText(business.business_description)

        if services.check_if_bookmark(services.app_session.user_id, services.app_session.business_id):
            self.ui.bookmark_button.setIcon(self.filled_icon)
            self.ui.bookmark_button.setChecked(True)
        else:
            self.ui.bookmark_button.setIcon(self.unfilled_icon)

        self.load_reviews()
        # reviews = services.get_reviews(business.id)

        # for review in reviews:
        #     review_icon = ReviewIcon(review)
        #     # card.clicked.connect()
        #     self.ui.review_holder.addWidget(review_icon)
        #     self.review_list.append(review_icon)
        #     # self.review_holder.append(card)

    def load_reviews(self):
        self.clear_reviews()
        reviews = services.get_reviews(services.app_session.get_business_id())

        for review in reviews:
            review_icon = ReviewIcon(review)
            # card.clicked.connect()
            self.ui.review_holder.addWidget(review_icon)
            self.review_list.append(review_icon)
            # self.review_holder.append(card)

    def clear_reviews(self):
        for review in self.review_list:
            review.deleteLater()
        
        self.review_list.clear()
    
    def open_review_editor(self):
        editor = ReviewEditor()
        editor.accepted.connect(self.load_reviews)
        editor.exec()

    def toggle_bookmark(self):
        user_id = services.app_session.get_user_id()
        business_id = services.app_session.get_business_id()
        services.toggle_bookmark(user_id, business_id)
        if self.ui.bookmark_button.isChecked():
            self.ui.bookmark_button.setIcon(self.filled_icon)
        else:
            self.ui.bookmark_button.setIcon(self.unfilled_icon)

class ReviewEditor(QDialog):
    def __init__(self): #
        # Initialize widget and load layout from its .ui file
        super().__init__()
        self.ui = review_editor()
        self.ui.setupUi(self)

        self.ui.rating_label.setText(f"{self.ui.rating_bar.value() / 2} ⭐")
        self.ui.rating_bar.valueChanged.connect(self.update_rating_text)
        self.accepted.connect(self.send_review)

    def update_rating_text(self):
        self.ui.rating_label.setText(f"{self.ui.rating_bar.value() / 2} ⭐")
        
    def send_review(self):
        user_id = services.app_session.get_user_id()
        business_id = services.app_session.get_business_id()
        rating = self.ui.rating_bar.value() / 2
        content = self.ui.review_content.toPlainText()
        
        services.add_review(user_id, business_id, rating, content)

class ProfilePage(QWidget):
    business_selected = Signal(object)
    def __init__(self):
        super().__init__()
        self.ui = profile_page()
        self.ui.setupUi(self)
        self.bookmark_list: list[BusinessCard] = []

    def load_profile(self, user_id):
        self.clear_bookmarks()
        username = services.get_username_from_id(user_id)
        if username is not None:
            self.ui.username_label.setText(username)
            bookmarks = services.get_bookmarks_by_user(user_id)
            for bookmark in bookmarks:
                business = services.get_business_from_id(bookmark.business_id)
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

