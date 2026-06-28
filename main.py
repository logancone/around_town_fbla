from database import create_tables

from PySide6.QtWidgets import QApplication
from gui.shell.main_window import MainWindow

from dev.uic_conversion import convert_ui_to_py

from dev.fake_data_generation import generate_all_fake_data, generate_some_fake_data

import os

def gui_init():
    app = QApplication()
    
    with open("resources/style.qss", "r", encoding='utf-8') as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()
    app.exec()

def main():
    if os.path.exists("app_database.db"):
        os.remove("app_database.db")

    create_tables()

    generate_all_fake_data()
    # generate_some_fake_data()

    gui_init()

if __name__ == "__main__":
    # convert_ui_to_py() #Remove for presentation!
    main()

