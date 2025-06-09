from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit

class TranscriptViewer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setPlaceholderText("Transcription will appear here...")

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        self.setLayout(layout)

    def set_transcription(self, transcription):
        """Set the transcription text in the viewer."""
        self.text_edit.setPlainText(transcription)
    
    def clear_transcription(self):
        """Clear the transcription text."""
        self.text_edit.clear()

    def append_transcription(self, text):
        """Append text to the existing transcription."""
        current_text = self.text_edit.toPlainText()
        self.text_edit.setPlainText(current_text + "\n" + text)