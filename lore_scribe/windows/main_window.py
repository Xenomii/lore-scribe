# lore_scribe/windows/main_window.py

from PySide6.QtWidgets import QMainWindow, QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lore Scribe")
        self.setGeometry(100, 100, 800, 600)

        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)
