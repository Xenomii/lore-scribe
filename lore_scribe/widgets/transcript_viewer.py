from PySide6.QtCore import Signal, Qt, QUrl
from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit

class TranscriptViewer(QWidget):
    file_dropped = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setPlaceholderText("🎧 Drag an audio file here to begin transcription.")
        self._default_style = self.styleSheet()

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        self.setLayout(layout)

        self.setAcceptDrops(True)
        self.setStyleSheet("border: 2px dashed #888; padding: 40px;")
    
    def dragEnterEvent(self, event):
        """Handle drag enter event to accept audio files."""
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                if url.isLocalFile() and url.toLocalFile().lower().endswith(('.mp3', '.wav', '.m4a', '.flac')):
                    self.setStyleSheet("border: 2px dashed green; padding: 40px;")
                    event.acceptProposedAction()
                    return
        event.ignore()

    def dragLeaveEvent(self, event):
        self.setStyleSheet(self._default_style)

    def dropEvent(self, event):
        """Handle drop event to process the dropped audio file."""
        self.setStyleSheet(self._default_style)
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                if url.isLocalFile():
                    file_path = url.toLocalFile()
                    self.file_dropped.emit(file_path)
                    self.set_transcription(f"File dropped: {file_path}")
                    return
        event.ignore()

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