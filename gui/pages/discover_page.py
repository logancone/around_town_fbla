from PySide6.QtWidgets import QWidget, QPushButton
from PySide6.QtCore import Signal, QTimer
from PySide6.QtGui import QFont

from database import Business
from services.business_services import get_all_businesses, run_search, get_distance_to_business
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

        self.ui.sort_dropdown.currentIndexChanged.connect(self.sort_dropdown_changed)
        self.ui.category_dropdown.currentIndexChanged.connect(self.category_dropdown_changed)
        self.ui.distance_dropdown.currentIndexChanged.connect(self.distance_dropdown_changed)

        self.ui.reset_button.clicked.connect(self.reset_parameters)
        
        # Creates a timer for the searchbar to add a short delay between keystrokes and running a search
        self.search_timer = QTimer()
        self.search_timer.setSingleShot(True)
        self.search_timer.timeout.connect(self.refresh_cards)

        self.ui.search_bar.textEdited.connect(self.on_text_edited)
        self.ui.search_bar.returnPressed.connect(self.refresh_cards)

        self.create_chat_button()
        self.chatbutton.clicked.connect(self.open_chat_window)

        self.chat_window = ChatWindow()

        self.sort_mode = "recommended"
        self.category_mode = "all_categories"
        self.distance_mode = "any_distance"
        


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

    def refresh_cards(self):
        data = self.all_business_data

        data = self.apply_search(data)
        data = self.apply_sort(data)
        data = self.apply_category(data)
        data = self.apply_distance(data)

        self.populate_cards(data)
        

    # Starts the search delay timer
    def on_text_edited(self):
        self.search_timer.start(200)

    def apply_search(self, data: list[Business]):
        if self.ui.search_bar == "":
            return data
        
        search_query = self.ui.search_bar.text().lower()
        return run_search(search_query, data)
    
    def apply_sort(self, data: list[Business]):
        if self.sort_mode == "recommended":
            return app_session.recommendation_service.sort_some_businesses_by_rec_score(data)
        elif self.sort_mode == "rating_desc":
            return sorted(data, key=lambda b: b.avg_rating, reverse=True)
        elif self.sort_mode == "rating_asc":
            return sorted(data, key=lambda b: b.avg_rating)
        elif self.sort_mode == "distance":
            if app_session.cur_lat is None or app_session.cur_lon is None:
                return data
            return sorted(data, key=lambda b: get_distance_to_business(b.id, app_session.cur_lat, app_session.cur_lon)) #type: ignore
        else:
            return data

    def apply_category(self, data: list[Business]):
        if self.category_mode == "all_categories":
            return data
        
        approved_businesses = []
        for business in data:
            if business.category == self.category_mode:
                approved_businesses.append(business)

        return approved_businesses

    def apply_distance(self, data: list[Business]):
        if self.distance_mode == "any_distance":
            return data
        if app_session.cur_lat is None or app_session.cur_lon is None:
            return data

        approved_businesses = []
        for business in data:
            business_dist = get_distance_to_business(business.id, app_session.cur_lat, app_session.cur_lon)
            max_dist = int(self.distance_mode.split("_")[0])

            if business_dist <= max_dist:
                approved_businesses.append(business)

        return approved_businesses


    
    def sort_dropdown_changed(self, new_index):
        modes = ["recommended", "rating_desc", "rating_asc", "distance"]
        self.sort_mode = modes[new_index]

        self.refresh_cards()
    
    def category_dropdown_changed(self, new_index):
        modes = ["all_categories", "retail", "food", "entertainment", "services"]
        self.category_mode = modes[new_index]

        self.refresh_cards()

    def distance_dropdown_changed(self, new_index):
        modes = ["any_distance", "5_miles", "10_miles", "25_miles", "50_miles"]
        self.distance_mode = modes[new_index]

        self.refresh_cards()
        

    # Emits the business_selected signal, containing the business (which is passed from the business_card class)
    def card_clicked(self, business):
        self.business_selected.emit(business)
    
    # Loads data from every single business and stores it in the class, allowing for quick reloading of business cards 
    def load_all_business_data(self):
        self.all_business_data = get_all_businesses()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.chatbutton.move(self.width() - 150, self.height() - 75)

    def create_chat_button(self):
        self.chatbutton = QPushButton("Ask AI\nAssistant💬", self)
        self.chatbutton.adjustSize()
        self.chatbutton.resize(125, 60)
        self.chatbutton.move(self.width() - 150, self.height() - 75)
        self.chatbutton.raise_()

    def open_chat_window(self):
        self.chat_window.show()

    def reset_parameters(self):
        self.ui.search_bar.setText("")

        self.ui.sort_dropdown.setCurrentIndex(0)
        self.ui.category_dropdown.setCurrentIndex(0)
        self.ui.distance_dropdown.setCurrentIndex(0)

        self.refresh_cards()