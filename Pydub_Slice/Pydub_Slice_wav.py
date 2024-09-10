from pydub import AudioSegment
import os

# Define the path to the MP3 file in t he directory "G:\Music\Pydub_Slice."
file_path = r"G:\Music\Pydub_Slice\Bon_Jovi_Waves.mp3"

# Load the MP3 file using Pydub
audio = AudioSegment.from_mp3(file_path)

# Duration of each slice in milliseconds (10 seconds = 10000 milliseconds.)
slice_length = 10000

# Total length of the audio in milliseconds.
audio_length = len(audio)

# Output directory for saving the slices (same as the input directory)
output_dir = os.path.dirname(file_path)

# Slice the audio into 3-second clips and save each one
for i in range(0, audio_length, slice_length):
    # Slice the audio segment
    clip = audio[i:i + slice_length]

    # Save each clip with a unique file name
    output_file = os.path.join(output_dir, f"Bon_Jovi_Waves_clip_{i // slice_length + 1}.mp3")
    clip.export(output_file, format="mp3")

print("Slicing complete!")
