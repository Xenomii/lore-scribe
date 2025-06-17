import whisper
import torch
from pathlib import Path
from typing import Union, Callable
import numpy as np

class Transcriber:
    def __init__(self, audio_path: Union[str, Path], model_size: str = "base", on_progress: Callable[[float], None] = None, initial_prompt: str = None):
        """ Initialize the Transcriber with the audio file path and model size.
        :param audio_path: Path to the audio file to be transcribed.
        :param model_size: Size of the Whisper model to use (e.g., "tiny", "base", "small", "medium", "large").
        """
        self.audio_path = audio_path
        self.model_size = model_size
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model_name = f"whisper-{model_size}-{self.device}"
        self.model = whisper.load_model(self.model_size, device=self.device)
        self.on_progress = on_progress
        self.initial_prompt = initial_prompt

    def transcribe(self) -> str:
        """ Transcribe the audio file using the Whisper model.
        :return: The transcribed text from the audio file.
        """

        if not Path(self.audio_path).is_file():
            raise FileNotFoundError(f"Audio file '{self.audio_path}' does not exist.")
        
        # Load and preprocess the audio file
        audio = whisper.load_audio(self.audio_path)
        duration_sec = len(audio) / whisper.audio.SAMPLE_RATE
        segment_size_sec = 30  # Process in segments of 30 seconds

        # Pad or trim the audio to ensure it matches the expected length
        audio = whisper.pad_or_trim(audio, length=int(duration_sec * whisper.audio.SAMPLE_RATE))

        chunks = np.arange(0, duration_sec, segment_size_sec)
        text_chunk = ""
        
        for i, start in enumerate(chunks):
            end = min(start + segment_size_sec, duration_sec)
            audio_chunk = audio[int(start * whisper.audio.SAMPLE_RATE):int(end * whisper.audio.SAMPLE_RATE)]

            result = self.model.transcribe(audio_chunk, language="en", verbose=True, fp16=False, initial_prompt=self.initial_prompt)
            text_chunk += result["text"] + " "

            if self.on_progress:
                progress = (end / duration_sec) * 100
                self.on_progress(progress)

        return text_chunk.strip()