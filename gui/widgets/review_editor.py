from PySide6.QtWidgets import QDialog

import services

from gui.generated.ui_review_editor import Ui_Dialog as review_editor

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
