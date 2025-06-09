# lore_scribe/windows/main_window.py

from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QTextEdit, QFileDialog
from lore_scribe.widgets.transcript_viewer import TranscriptViewer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lore Scribe")
        self.setGeometry(100, 100, 800, 600)
        
        # Central widget & layout
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Upload file button
        self.upload_button = QPushButton("Upload Audio File")
        self.upload_button.clicked.connect(self.upload_audio_file)
        layout.addWidget(self.upload_button)

        # Transcription text area
        self.transcript_viewer = TranscriptViewer()
        layout.addWidget(self.transcript_viewer)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
    def upload_audio_file(self):
        file_path, _ =QFileDialog.getOpenFileName(self, "Select Audio File", filter="Audio Files (*.mp3 *.wav *.flac *.m4a);;All Files (*)")
        if file_path:
            self.transcribe_audio(file_path)

    def transcribe_audio(self, file_path):
        # Placeholder for transcription logic
        # In a real application, you would call the transcription service here
        self.transcript_viewer.set_transcription(f"Transcribing audio file: {file_path}\n\n(Transcription result will appear here...)")
        # Simulate transcription result
        self.transcript_viewer.append_transcription("This is a simulated transcription of the audio file.")