from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, QTimer

from database import Business
from services.business_services import get_all_businesses, run_search

from gui.generated.ui_discover_page import Ui_Form as discover_page

from gui.widgets.business_card import BusinessCard

# Represents the discover page, which is where business cards are displayed for the user to search through
class DiscoverPage(QWidget):
    # Creates a signal that will tell the navshell when to open the business page and what business to display
    business_selected = Signal(object)

    # Initialize class and load ui
    def __init__(self):
        super().__init__()
        self.ui = discover_page()
        self.ui.setupUi(self)

        # Creates a list of the raw business data and the active cards, which important for sorting, filtering, and cleanup
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

    # Removes all cards from the discover page
    def clear_cards(self):
        for card in self.card_list:
            card.deleteLater()
        self.card_list.clear()

    # Clears and loads cards from a list of BusinessData objects
    def populate_cards(self, businesses):
        self.clear_cards()

        for i, business in enumerate(businesses):
            card = BusinessCard(business)
            card.clicked.connect(self.card_clicked)
            self.ui.grid_layout.addWidget(card, i//3, i%3)
            self.card_list.append(card)

    def on_text_edited(self):
        self.search_timer.start(200)

    def run_search(self):
        self.clear_cards()
        self.populate_cards(run_search(self.ui.search_bar.text().lower()))
        

    def filter_cards_by_category(self, category):
        approved_businesses = []
        for business in self.all_business_data:
            if business.category == category:
                approved_businesses.append(business)

        self.populate_cards(approved_businesses)
    
    def sort_cards_by_rating(self, descending):
        sorted_businesses = sorted(self.all_business_data, key=lambda b: b.avg_rating, reverse=descending)
        self.populate_cards(sorted_businesses)

    def card_clicked(self, business):
        self.business_selected.emit(business)
 
    def load_all_business_data(self):
        self.all_business_data = get_all_businesses()
