from pydub import AudioSegment

SUPPORTED_FORMATS = ['.mp3', '.wav', '.m4a', '.flac']

def validate_audio_file(file_path: str) -> tuple[str, bool, int]:
    """Check if the given file is a valid audio file.
    Args:
        file_path (str): Path to the audio file.
    Returns:
        bool: True if the file is a valid audio file, False otherwise.
    """
    print(f"[Validation] Started validating: {file_path}")
    try:
        audio = AudioSegment.from_file(file_path)
        print(f"[Validation] Duration: {len(audio)} ms")
        return (file_path, True, len(audio))
    except Exception as e:
        print(f"[Validation] Failed: {e}")
        print(f"Error loading audio file {file_path}: {e}")
        return (file_path, False, -1)