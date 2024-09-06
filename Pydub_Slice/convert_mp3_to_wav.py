## FFmpeg needs added for Pydub to work
## https://phoenixnap.com/kb/ffmpeg-windows

from os.path import realpath

from pydub import AudioSegment
import os

# Define the path to the MP3 file
mp3_file_path = r"G:\Music\Bon_Jovi_Waves.mp3"

# Load the MP3 file
audio = AudioSegment.from_mp3(mp3_file_path)

# Define the output path for the WAV file (same directory, different extension)
wav_file_path = os.path.splitext(mp3_file_path)[0] + ".wav"

# Export the audio as a WAV file
audio.export(wav_file_path, format="wav")

print(f"Conversion complete! WAV file saved at: {wav_file_path}")
