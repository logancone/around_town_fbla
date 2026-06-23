from PySide6.QtWidgets import QFrame, QLabel, QDialog
from PySide6.QtCore import Qt, QTimer

from services.user_services import get_username_from_id, AIService, AIWorker

from gui.generated.ui_chat_window import Ui_Form as chat_window

from app_session import app_session

class ChatWindow(QDialog):
    def __init__(self):
        # Initialize class and setup ui
        super().__init__()

        self.ui = chat_window()
        self.ui.setupUi(self)

        self.ai_service = AIService()

        self.chat_layout = self.ui.scrollAreaWidgetContents.layout()
        assert self.chat_layout
        self.chat_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        self.ui.send_button.clicked.connect(self.send_chat)
        # self.ui.chat_input.returnPressed.connect(self.send_chat)
        
    def verify_chat(self):
        message = self.ui.chat_input.text()
        if len(message) > 0 and len(message) < 1000:
            return True
        elif len(message) > 0:
            self.ui.warning_label.setText("Chat must be less than 1000 characters!")
            return False
        else:
            self.ui.warning_label.setText("Chat cannot be empty!")
            return False

    def send_chat(self):
        if not self.verify_chat():
            return
        
        self.ui.send_button.setEnabled(False)

        user_chat = self.ui.chat_input.text()
        self.add_chat_label("user", user_chat)
        self.ui.chat_input.clear()

        self.start_loading_anim()

        self.worker = AIWorker(self.ai_service, user_chat, app_session.recommendation_service)
        self.worker.finished.connect(lambda x: self.add_chat_label("ai", x))
        self.worker.error.connect(self.ai_error)

        self.worker.start()

        
    
    def add_chat_label(self, sender, message):
        assert sender == "user" or sender == "ai"
        assert self.chat_layout

        new_label = QLabel(message)
        new_label.setWordWrap(True)

        self.chat_layout.addWidget(new_label)

        if sender == "user":
            new_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        else:
            new_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

            self.ui.send_button.setEnabled(True)
            self.loading_timer.stop()
            self.loading_label.deleteLater()
        
        QTimer.singleShot(10, self.scroll_to_bottom)

        
    def ai_error(self, error):
        self.ui.warning_label.setText(error)
        self.ui.send_button.setEnabled(True)
        self.loading_timer.stop()
        self.loading_label.deleteLater()

    def start_loading_anim(self):
        assert self.chat_layout

        self.loading_label = QLabel("Thinking")
        self.chat_layout.addWidget(self.loading_label)

        self.dots = 0

        self.loading_timer = QTimer()
        self.loading_timer.timeout.connect(self.update_loading_anim)
        self.loading_timer.start(400)

    def update_loading_anim(self):
        self.dots = (self.dots + 1) % 4
        self.loading_label.setText("Thinking" + "." * self.dots)

    def scroll_to_bottom(self):
        scrollbar = self.ui.scrollArea.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())