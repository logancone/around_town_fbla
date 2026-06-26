from PySide6.QtWidgets import QDialog

from services.user_services import generate_user_report

from app_session import app_session

from gui.generated.ui_report_editor import Ui_Dialog as report_editor

# Represents the dialog popup that allows users to give businesses ratings and write reviews
class ReportEditor(QDialog):
    # Initialize class and setup ui
    def __init__(self):
        super().__init__()
        self.ui = report_editor()
        self.ui.setupUi(self)
        

        self.accepted.connect(self.download_report)

    def download_report(self):
        user_id = app_session.user_id

        user_info = self.ui.user_info.isChecked()
        bookmarked_businesses = self.ui.bookmarked_businesses.isChecked()
        owned_businesses = self.ui.owned_businesses.isChecked()
        review_history = self.ui.review_history.isChecked()
        
        generate_user_report(user_id, user_info, bookmarked_businesses, owned_businesses, review_history)
        


