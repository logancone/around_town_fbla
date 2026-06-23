from PySide6.QtWidgets import QWidget, QPushButton
from PySide6.QtCore import Signal, QTimer
from PySide6.QtGui import QFont

from database import Business
from services.business_services import get_all_businesses, run_search
# from services.user_services import get_recommendation_score

from app_session import app_session

from gui.generated.ui_discover_page import Ui_Form as discover_page

from gui.widgets.business_card import BusinessCard
from gui.widgets.chat_window import ChatWindow

# Represents the discover page, which is where business cards are displayed for the user to search through
class DiscoverPage(QWidget):
    # Creates a signal that will tell the navshell when to open the business page and what business to display
    business_selected = Signal(object)

    # Initialize class and setup ui
    def __init__(self):
        super().__init__()
        self.ui = discover_page()
        self.ui.setupUi(self)

        # Creates a list of the raw business objects and the active cards, which important for sorting, filtering, and cleanup
        self.all_business_data : list[Business] = []
        self.card_list : list[BusinessCard] = []

        self.ui.retail_button.clicked.connect(lambda: self.filter_cards_by_category("Retail"))
        self.ui.food_button.clicked.connect(lambda: self.filter_cards_by_category("Food"))
        self.ui.entertainment_button.clicked.connect(lambda: self.filter_cards_by_category("Entertainment"))
        self.ui.services_button.clicked.connect(lambda: self.filter_cards_by_category("Services"))

        self.ui.ratings_descending_button.clicked.connect(lambda: self.sort_cards_by_rating(True))
        self.ui.ratings_ascending_button.clicked.connect(lambda: self.sort_cards_by_rating(False))
        
        # Creates a timer for the searchbar to add a short delay between keystrokes and running a search
        self.search_timer = QTimer()
        self.search_timer.setSingleShot(True)
        self.search_timer.timeout.connect(self.run_search)

        self.ui.search_bar.textEdited.connect(self.on_text_edited)

        # self.ui.chat_button.setParent(self)
        # self.ui.chat_button.raise_()
        # self.ui.chat_button.move(self.width() - 70, self.height() - 70)

        self.chatbutton = QPushButton("Ask AI\nAssistant💬", self)
        self.chatbutton.adjustSize()
        # font1 = QFont()
        # font1.setPointSize(1)
        # self.chatbutton.setFont(font1)
        self.chatbutton.resize(125, 60)
        self.chatbutton.move(self.width() - 150, self.height() - 75)
        self.chatbutton.raise_()

        self.chatbutton.clicked.connect(self.open_chat_window)
        self.chat_window = ChatWindow()

    # Removes all cards from the discover page
    def clear_cards(self):
        for card in self.card_list:
            card.deleteLater()
        self.card_list.clear()

    # Clears cards and loads news cards from a list of Business objects
    def populate_cards(self, businesses):
        self.clear_cards()

        for i, business in enumerate(businesses):
            card = BusinessCard(business)
            card.clicked.connect(self.card_clicked)
            self.ui.grid_layout.addWidget(card, i//3, i%3)
            self.card_list.append(card)

    # Starts the search delay timer
    def on_text_edited(self):
        self.search_timer.start(200)

    # Clears cards and then runs a search with the current text in the serach bar, populating the page with the results
    def run_search(self):
        self.clear_cards()
        self.populate_cards(run_search(self.ui.search_bar.text().lower()))
        
    # Goes through all businesses, selecting the ones of a certain category, and populates the page with the results
    def filter_cards_by_category(self, category):
        approved_businesses = []
        for business in self.all_business_data:
            if business.category == category:
                approved_businesses.append(business)

        self.populate_cards(approved_businesses)
    
    # Sorts all businesses by their rating (descending if param=True, else ascending), and populates the page with the results
    def sort_cards_by_rating(self, descending):
        sorted_businesses = sorted(self.all_business_data, key=lambda b: b.avg_rating, reverse=descending)
        self.populate_cards(sorted_businesses)

    def sort_cards_by_recommendation(self):
        sorted_businesses = app_session.recommendation_service.sort_businesses_by_rec_score()
        self.populate_cards(sorted_businesses)

    # Emits the business_selected signal, containing the business (which is passed from the business_card class)
    def card_clicked(self, business):
        self.business_selected.emit(business)
    
    # Loads data from every single business and stores it in the class, allowing for quick reloading of business cards 
    def load_all_business_data(self):
        self.all_business_data = get_all_businesses()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.chatbutton.move(self.width() - 150, self.height() - 75)

    def open_chat_window(self):
        self.chat_window.show()