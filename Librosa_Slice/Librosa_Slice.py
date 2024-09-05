import librosa
import soundfile as sf
import os

# Define the path to the MP3 file in the directory "G:\Music\Librosa_Slice"
file_path = r"G:\Music\Librosa_Slice\Bon_Jovi_Waves.mp3"

# Load the MP3 file (y = waveform, sr = sample rate)
y, sr = librosa.load(file_path, sr=None)

# Duration of each clip in seconds
clip_duration = 10

# Calculate the number of samples in each 3-second clip
samples_per_clip = clip_duration * sr

# Total number of clips
num_clips = len(y) // samples_per_clip

# Output directory for the clips (same as input directory)
output_dir = os.path.dirname(file_path)

# Slice and save each clip
for i in range(num_clips):
    # Slice the waveform
    start_sample = i * samples_per_clip
    end_sample = start_sample + samples_per_clip
    clip = y[start_sample:end_sample]

    # Save each clip as a separate audio file
    output_file = os.path.join(output_dir, f"Bon_Jovi_Waves_clip_{i + 1}.mp3")
    sf.write(output_file, clip, sr)

print("Slicing complete!")
