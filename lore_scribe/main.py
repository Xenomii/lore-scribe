# lore_scribe/main.py

from PySide6.QtWidgets import QApplication
from lore_scribe.windows.main_window import MainWindow
import sys

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
