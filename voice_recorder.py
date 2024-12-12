import sounddevice as sd
from scipy.io.wavfile import write
import os

def record_audio(output_file, duration=5, sample_rate=16000):
    print(f"Recording for {duration} seconds...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()  # Wait for the recording to finish
    write(output_file, sample_rate, audio_data)
    print(f"Recording saved to {output_file}")

if __name__ == "__main__":
    user = input("Enter the user name (e.g., user1, user2): ")
    os.makedirs(f"data/{user}", exist_ok=True)
    filename = f"data/{user}/sample.wav"
    record_audio(filename)
