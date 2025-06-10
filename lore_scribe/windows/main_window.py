# lore_scribe/windows/main_window.py

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox
from lore_scribe.widgets.transcript_viewer import TranscriptViewer
from lore_scribe.services.audio_validation import validate_audio_file
from lore_scribe.services.task_runner import TaskRunner

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lore Scribe")
        self.setGeometry(100, 100, 800, 600)
        
        # Central widget & layout
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Transcript viewer
        self.transcript_viewer = TranscriptViewer()
        self.transcript_viewer.file_dropped.connect(self.on_file_dropped)
        layout.addWidget(self.transcript_viewer)

        # Task runner for background processing
        self.task_runner = TaskRunner()

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def on_file_dropped(self, file_path: str):
        """Handle the file dropped event."""
        print(f"[MainWindow] File dropped: {file_path}")
        self.transcript_viewer.set_transcription("🔍 Verifying audio file... Please wait.")

        print("[MainWindow] Starting background validation...")
        QTimer.singleShot(50, lambda:self.task_runner.run_task(
            validate_audio_file, 
            file_path, 
            on_result=self.on_file_validation_result, 
            on_error=self.on_file_validation_error
        ))

    def on_file_validation_result(self, result: tuple[str, bool, int]):
        """Handle the result of the audio file validation."""
        file_path, is_valid, duration = result
        if is_valid:
            self.transcript_viewer.append_transcription(f"✅ Audio file '{file_path}' is valid. Duration: {duration} ms")
            self.transcribe_audio(file_path)
        else:
            QMessageBox.warning(self, "Invalid File", f"The file '{file_path}' is not a valid audio file.")

    def on_file_validation_error(self, error: Exception):
        """Handle any errors that occur during audio file validation."""
        QMessageBox.critical(self, "Error", f"An error occurred while validating the audio file: {error}")
        self.transcript_viewer.append_transcription("❌ Error validating audio file. Please try again.")
        
    def transcribe_audio(self, file_path):
        # Placeholder for transcription logic
        # In a real application, you would call the transcription service here
        self.transcript_viewer.append_transcription(f"Transcribing audio file: {file_path}\n\n(Transcription result will appear here...)")
        # Simulate transcription result
        self.transcript_viewer.append_transcription("This is a simulated transcription of the audio file.")