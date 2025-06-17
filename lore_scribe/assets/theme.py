# assets/theme.py

APP_STYLESHEET = """
QMainWindow {
    background-color: #FAFAFA;
}
QTextEdit {
    background-color: #FFFFFF;
    color: #212121;
    font-size: 14px;
    border: 1px solid #BDBDBD;
    border-radius: 6px;
    padding: 6px;
}
QPushButton {
    background-color: #e6c8f2;
    color: #4a235a;
    border: 1px solid #d6a9e2;
    border-radius: 6px;
    padding: 6px 12px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #f0d9f8;
}
QMessageBox {
    background-color: #FFFFFF;
    color: #212121;
    font-size: 13px;
}
QProgressBar {
    border: 2px solid #e6c8f2;
    border-radius: 10px;
    background-color: #f8f1fc;
    height: 20px;
    text-align: center;
    color: #4a235a;
    font-weight: bold;
}

QProgressBar::chunk {
    background-color: #e6c8f2;
    border-radius: 8px;
    margin: 1px;
}
"""

DARK_APP_STYLESHEET = """
QMainWindow {
    background-color: #121212;
}
QTextEdit {
    background-color: #1E1E1E;
    color: #EEEEEE;
    font-size: 14px;
    border: 1px solid #333;
    border-radius: 6px;
    padding: 6px;
}
QProgressBar {
    border: 2px solid #a94dc1;
    border-radius: 10px;
    background-color: #1c1c1c;
    height: 20px;
    text-align: center;
    color: #f3e6f8;
    font-weight: bold;
}

QProgressBar::chunk {
    background-color: #a94dc1;
    border-radius: 8px;
    margin: 1px;
}
QMessageBox {
    background-color: #1E1E1E;
    color: #EEEEEE;
    font-size: 13px;
}
"""
