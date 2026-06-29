from PySide6.QtWidgets import QDialog

from services.user_services import generate_user_report

from app_session import app_session

from gui.generated.ui_location_editor import Ui_Dialog as location_editor

# Represents the dialog popup that allows users to give businesses ratings and write reviews
class LocationEditor(QDialog):
    # Initialize class and setup ui
    def __init__(self):
        super().__init__()
        self.ui = location_editor()
        self.ui.setupUi(self)
        

        self.ui.ok_button.clicked.connect(self.set_new_location)
        self.ui.cancel_button.clicked.connect(super().reject)
        self.ui.restore_defaults_button.clicked.connect(self.restore_defaults)


    # Returns true if input is valid, else returns false
    def validate_input(self) -> bool:
        if self.ui.latitude_input.text() != "" and self.ui.longitude_input.text() != "":
            try:
                float(self.ui.latitude_input.text().strip())
                float(self.ui.longitude_input.text().strip())
                return True
            except:
                return False
        else:
            return False       

    # 
    def set_new_location(self):
        if self.validate_input():
            app_session.update_user_location(float(self.ui.latitude_input.text().strip()), float(self.ui.longitude_input.text().strip()))
            super().accept()
        else:
            self.ui.error_label.setText("Invalid Input! Please try again.")

    def restore_defaults(self):
        self.ui.latitude_input.setText("37.0479891178922")
        self.ui.longitude_input.setText("-76.4984552293407")