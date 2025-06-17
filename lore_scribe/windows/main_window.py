# lore_scribe/windows/main_window.py

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QMessageBox, QPushButton
from lore_scribe.widgets.transcript_viewer import TranscriptViewer
from lore_scribe.services.audio_validation import validate_audio_file
from lore_scribe.services.task_runner import TaskRunner
from lore_scribe.services.transcription import Transcriber
from lore_scribe.assets.theme import APP_STYLESHEET, DARK_APP_STYLESHEET

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lore Scribe")
        self.setGeometry(100, 100, 800, 600)

        # Central widget & layout
        central_widget = QWidget()
        layout = QVBoxLayout()

        self.current_theme = "dark"  # Default theme
        self.apply_theme()

        self.toggle_theme_button = QPushButton("Switch Themes")
        self.toggle_theme_button.clicked.connect(self.toggle_theme)  # Placeholder for theme toggle button
        layout.addWidget(self.toggle_theme_button)

        # Transcript viewer
        self.transcript_viewer = TranscriptViewer()
        self.transcript_viewer.file_dropped.connect(self.on_file_dropped)
        layout.addWidget(self.transcript_viewer)

        # Task runner for background processing
        self.task_runner = TaskRunner()

        self.transcriber = None  # Will be initialized per audio file

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
       
    def apply_theme(self):
        """Apply the current theme to the main window."""
        if self.current_theme == "dark":
            self.setStyleSheet(DARK_APP_STYLESHEET)
        else:
            self.setStyleSheet(APP_STYLESHEET)

    def toggle_theme(self):
        """Toggle between light and dark themes."""
        if self.current_theme == "dark":
            self.current_theme = "light"
        else:
            self.current_theme = "dark"
        self.apply_theme()
        print(f"[MainWindow] Theme switched to: {self.current_theme}")    

    def on_file_dropped(self, file_path: str):
        """Handle the file dropped event."""
        print(f"[MainWindow] File dropped: {file_path}")
        self.transcript_viewer.set_transcription("🔍 Verifying audio file... Please wait.")

        print("[MainWindow] Starting background validation...")
        QTimer.singleShot(50, lambda: self.task_runner.run_task(
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
        """Transcribe the audio file using the Transcriber service."""
        self.transcript_viewer.append_transcription(f"🎤 Transcribing audio file '{file_path}'... Please wait.")
        self.transcript_viewer.set_progress(0)

        print("[MainWindow] Initializing Transcriber..." )
        self.transcriber = Transcriber(file_path, on_progress=self.on_transcription_progress)

        print("[MainWindow] Starting transcription...")
        QTimer.singleShot(50, lambda: self.task_runner.run_task(
            self.transcriber.transcribe,
            on_result=self.on_transcription_result,
            on_error=self.on_transcription_error
        ))

    def on_transcription_result(self, transcription: str):
        """Handle the result of the transcription."""
        print("[MainWindow] Transcription completed.")
        self.transcript_viewer.append_transcription(transcription)

    def on_transcription_error(self, error: Exception):
        """Handle any errors that occur during transcription."""
        QMessageBox.critical(self, "Error", f"An error occurred during transcription: {error}")
        self.transcript_viewer.append_transcription("❌ Error during transcription. Please try again.")

    def on_transcription_progress(self, progress: float):
        """Update the transcription progress in the transcript viewer."""
        self.transcript_viewer.set_progress(progress)
        print(f"[MainWindow] Transcription progress: {progress:.2f}%")
