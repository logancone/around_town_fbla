from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel, QGridLayout, QSizePolicy, QMainWindow, QStackedWidget, QFrame, QTextEdit, QVBoxLayout, QScrollArea, QDialog
from PySide6.QtCore import QFile, Signal, Qt
from PySide6.QtGui import QMouseEvent, QPixmap

from database import Business, Review
from services import authenticate_user, get_rating_str, get_businesses_all, get_username_from_id, get_reviews, get_businesses_by_category, sort_businesses_by_rating, is_username_available, add_user

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_file = QFile("ui/main_window.ui")
        loader = QUiLoader()

        self.ui = loader.load(ui_file)
        ui_file.close()
        
        self.outer_stack = self.ui.findChild(QStackedWidget, "outer_stack")
        
        assert self.outer_stack is not None

        # Establish pages
        self.login_page = LoginPage()
        self.signup_page = SignupPage()
        self.nav_shell = NavShell()
        
        self.outer_stack.addWidget(self.login_page)
        self.outer_stack.addWidget(self.signup_page)
        self.outer_stack.addWidget(self.nav_shell)

        self.outer_stack.setCurrentWidget(self.login_page)

        self.login_page.login_success.connect(self.set_nav_shell)
        self.login_page.signup_request.connect(self.set_signup_page)
        self.signup_page.signup_success.connect(self.set_nav_shell)
        self.signup_page.login_request.connect(self.set_login_page)

        self.nav_shell.logout.connect(self.set_login_page)

    def set_login_page(self):
        assert self.outer_stack is not None
        self.outer_stack.setCurrentWidget(self.login_page)
    
    def set_signup_page(self):
        assert self.outer_stack is not None
        self.outer_stack.setCurrentWidget(self.signup_page)

    def set_nav_shell(self):
        assert self.outer_stack is not None
        self.outer_stack.setCurrentWidget(self.nav_shell)
    
class NavShell(QWidget):
    logout = Signal()
    def __init__(self):
        super().__init__()
        ui_file = QFile("ui/nav_shell.ui")
        loader = QUiLoader()

        loader.load(ui_file, self)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        # Get the root widget that was loaded
        root_widget = self.findChild(QWidget, "Form")
        if root_widget:
            layout.addWidget(root_widget)
        ui_file.close()

        self.page_stack = self.findChild(QStackedWidget, "page_stack")
        self.navbar = self.findChild(QFrame, "navbar")

        
        self.discover_button = self.findChild(QPushButton, "discover_button")
        self.logout_button = self.findChild(QPushButton, "logout_button")

        assert self.discover_button and self.logout_button and self.page_stack is not None

        self.discover_button.clicked.connect(self.set_discover_page)
        self.logout_button.clicked.connect(self.logout.emit)

        # Establish pages
        self.discover_page = DiscoverPage()
        self.business_page = BusinessPage()

        self.page_stack.addWidget(self.discover_page)
        self.page_stack.addWidget(self.business_page)

        self.discover_page.populate_cards(get_businesses_all())
        self.page_stack.setCurrentWidget(self.discover_page)

        self.discover_page.business_selected.connect(self.set_business_page)
        
    def set_discover_page(self):
        assert self.page_stack is not None

        self.discover_page.populate_cards(get_businesses_all())
        self.page_stack.setCurrentWidget(self.discover_page)

    def set_business_page(self, business):
        assert self.page_stack is not None

        self.business_page.set_to_business(business)
        self.page_stack.setCurrentWidget(self.business_page)

class LoginPage(QWidget):
    login_success = Signal()
    signup_request = Signal()

    def __init__(self):
        super().__init__()
        ui_file = QFile("ui/login_page.ui")
        loader = QUiLoader()

        loader.load(ui_file, self)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        # Get the root widget that was loaded
        root_widget = self.findChild(QWidget, "Form")
        if root_widget:
            layout.addWidget(root_widget)
        ui_file.close()

        self.username_entry = self.findChild(QLineEdit, "username_entry")
        self.password_entry = self.findChild(QLineEdit, "password_entry")
        
        self.error_label = self.findChild(QLabel, "error_label")

        self.login_button = self.findChild(QPushButton, "login_button")
        self.signup_button = self.findChild(QPushButton, "signup_button")

        # assert self.username_entry and self.password_entry is not None

        assert self.login_button and self.signup_button is not None

        self.login_button.clicked.connect(self.attempt_login)
        self.signup_button.clicked.connect(self.signup_request.emit)

    # Return True if username and password are valid inputs, else return false
    def validate_login_input(self, username, password):
        assert self.error_label is not None

        # Ensure both fields have text
        if len(username) == 0 or len(password) == 0:
            self.error_label.setText("Please fill out all fields!")
            return False

        return True
    
    def attempt_login(self):
        assert self.error_label and self.username_entry and self.password_entry is not None

        username = self.username_entry.text()
        password = self.password_entry.text()
        # If both fields have valid inputs
        if self.validate_login_input(username, password) == True:
            user = authenticate_user(username, password)

            if user is None:
                self.error_label.setText("Invalid username or password!")
            else:
                self.error_label.setText("Success!")
                self.login_success.emit()

class SignupPage(QWidget):
    signup_success = Signal()
    login_request = Signal()

    def __init__(self):
        super().__init__()
        ui_file = QFile("ui/signup_page.ui")
        loader = QUiLoader()

        loader.load(ui_file, self)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        # Get the root widget that was loaded
        root_widget = self.findChild(QWidget, "Form")
        if root_widget:
            layout.addWidget(root_widget)
        ui_file.close()

        self.username_entry = self.findChild(QLineEdit, "username_entry")
        self.password_entry = self.findChild(QLineEdit, "password_entry")
        self.confirm_password_entry = self.findChild(QLineEdit, "confirm_password_entry")
        
        self.error_label = self.findChild(QLabel, "error_label")

        self.signup_button = self.findChild(QPushButton, "signup_button")
        self.login_button = self.findChild(QPushButton, "login_button")
        
        # assert self.username_entry and self.password_entry is not None

        assert self.login_button and self.signup_button is not None

        self.signup_button.clicked.connect(self.attempt_signup)
        self.login_button.clicked.connect(self.login_request.emit)

    # Return True if username and password are valid inputs, else return false
    def validate_signup_input(self, username, password, confirm_password):
        assert self.error_label is not None

        # Ensure both fields have text
        if len(username) == 0 or len(password) == 0:
            self.error_label.setText("Please fill out all fields!")
            return False

        # Ensure username is between 4-25 characters
        if len(username) < 4 or len(username) > 25:
            self.error_label.setText("Ensure username is between 4-25 characters!")
            return False
        
        # Ensure password is between 4-35 characters
        if len(username) < 4 or len(username) > 35:
            self.error_label.setText("Ensure password is between 4-35 characters!")
            return False
        
        # Ensure password and confirm password match
        if password != confirm_password:
            self.error_label.setText("Both passwords must match!")
            return False
        
        # Ensure username is unique
        if is_username_available(username) == False:
            self.error_label.setText("Username is already taken!")
            return False
        
        return True
    
    def attempt_signup(self):
        assert self.error_label and self.username_entry and self.password_entry and self.confirm_password_entry is not None

        username = self.username_entry.text()
        password = self.password_entry.text()
        confirm_password = self.confirm_password_entry.text()

        # If both fields have valid inputs
        if self.validate_signup_input(username, password, confirm_password) == True:
            add_user(username, password)
            self.error_label.setText("Success!")
            self.signup_success.emit()


# Class for the business cards that populate discover page
class BusinessCard(QWidget):
    # create a click signal to notify when this card is clicked, passing the business object
    clicked = Signal(object)

    def __init__(self, business: Business): #Business object that is represented by this card
        # Initialize widget and load layout from its .ui file
        super().__init__()

        ui_file = QFile("ui/business_card.ui")
        loader = QUiLoader()

        loader.load(ui_file, self)
        ui_file.close()

        # Set size
        self.setFixedSize(200, 100)
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        # Define attributes
        self.title = self.findChild(QLabel, "title")
        self.category = self.findChild(QLabel, "category")
        self.ratings = self.findChild(QLabel, "ratings")
        self.thumbnail = self.findChild(QLabel, "thumbnail")

        # Assert everything has been defined (type-matching)
        assert self.title and self.category and self.ratings and self.thumbnail is not None

        # Set info/text
        self.business = business

        self.id = business.id

        self.title.setText(business.name)
        self.category.setText(business.category)
        self.ratings.setText(get_rating_str(business.id))

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
                self.thumbnail.width(),
                self.thumbnail.height(),
                Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                Qt.TransformationMode.SmoothTransformation
            )
        if square is not None:
            self.thumbnail.setPixmap(square)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.clicked.emit(self.business)
        return super().mousePressEvent(event)

# Class for the discover page
class DiscoverPage(QWidget):
    business_selected = Signal(object)

    def __init__(self):
        # Init class and load ui
        super().__init__()
        ui_file = QFile("ui/discover_page.ui")
        loader = QUiLoader()

        loader.load(ui_file, self)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        # Get the root widget that was loaded
        root_widget = self.findChild(QWidget, "Form")
        if root_widget:
            layout.addWidget(root_widget)
        ui_file.close()

        self.search_bar = self.findChild(QLineEdit, "search_bar")

        self.retail_button = self.findChild(QPushButton, "retail_button")
        self.food_button = self.findChild(QPushButton, "food_button")
        self.entertainment_button = self.findChild(QPushButton, "entertainment_button")
        self.services_button = self.findChild(QPushButton, "services_button")

        self.ratings_descending_button = self.findChild(QPushButton, "ratings_descending_button")
        self.ratings_ascending_button = self.findChild(QPushButton, "ratings_ascending_button")

        self.business_list = self.findChild(QWidget, "business_list")
        self.grid_layout = self.findChild(QGridLayout, "grid_layout")

        self.card_list : list[BusinessCard] = []

        assert self.retail_button and self.food_button and self.entertainment_button and self.services_button is not None

        self.retail_button.clicked.connect(lambda: self.filter_cards_by_category("Retail"))
        self.food_button.clicked.connect(lambda: self.filter_cards_by_category("Food"))
        self.entertainment_button.clicked.connect(lambda: self.filter_cards_by_category("Entertainment"))
        self.services_button.clicked.connect(lambda: self.filter_cards_by_category("Services"))

        assert self.ratings_descending_button and self.ratings_ascending_button is not None

        self.ratings_descending_button.clicked.connect(lambda: self.sort_cards_by_rating(False))
        self.ratings_ascending_button.clicked.connect(lambda: self.sort_cards_by_rating(True))
        

    def populate_cards(self, businesses):
        self.clear_cards()
        assert self.grid_layout is not None

        for i, business in enumerate(businesses):
            card = BusinessCard(business)
            card.clicked.connect(self.card_clicked)
            self.grid_layout.addWidget(card, i//3, i%3)
            self.card_list.append(card)

    def clear_cards(self):
        for card in self.card_list:
            card.deleteLater()
        self.card_list.clear()

    def filter_cards_by_category(self, category):
        self.populate_cards(get_businesses_by_category(category))
    
    def sort_cards_by_rating(self, ascending):
        self.populate_cards(sort_businesses_by_rating(ascending))

    def card_clicked(self, business):
        self.business_selected.emit(business)

# Class for the review icons that populate business page
class ReviewIcon(QWidget):
    def __init__(self, review: Review):
        # Init class and load .ui
        super().__init__()

        ui_file = QFile("ui/review_icon.ui")
        loader = QUiLoader()

        loader.load(ui_file, self)
        ui_file.close()

        # Set size
        self.setFixedSize(800, 100)
        # self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        # Define attributes
        self.header = self.findChild(QLabel, "header")
        self.body = self.findChild(QLabel, "body")

        # Assert everything has been defined (type-matching)
        assert self.header and self.body is not None

        # Set info/text
        header_text = f"{get_username_from_id(review.user_id)}: ⭐{review.rating}"
        self.header.setText(header_text)
        self.body.setText(review.content)

class BusinessPage(QWidget):
    def __init__(self):
        # Init class and load ui
        super().__init__()
        ui_file = QFile("ui/business_page.ui")
        loader = QUiLoader()

        loader.load(ui_file, self)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        # Get the root widget that was loaded
        root_widget = self.findChild(QWidget, "Form")
        if root_widget:
            layout.addWidget(root_widget)
        ui_file.close()

        self.title = self.findChild(QLabel, "title")
        self.description = self.findChild(QLabel, "description")
        self.review_holder = self.findChild(QVBoxLayout, "review_holder")
        self.add_review_button = self.findChild(QPushButton, "add_review_button")

        self.review_list: list[ReviewIcon] = []
        
        
    def set_to_business(self, business: Business):
        self.clear_reviews()
        assert self.title and self.description and self.review_holder is not None
        self.title.setText(business.name)
        self.description.setText(business.business_description)

        reviews = get_reviews(business.id)

        for review in reviews:
            review_icon = ReviewIcon(review)
            # card.clicked.connect()
            self.review_holder.addWidget(review_icon)
            self.review_list.append(review_icon)
            # self.review_holder.append(card)

    def clear_reviews(self):
        for review in self.review_list:
            review.deleteLater()
        
        self.review_list.clear()

