import sounddevice as sd
import wave
import os

def record_voice(filename="sample.wav", duration=5, sample_rate=44100):
    print(f"Enregistrement en cours... Parlez pendant {duration} secondes.")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()  # Attend la fin de l'enregistrement
    
    # Sauvegarde du fichier audio
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)  # Mono
        wf.setsampwidth(2)  # 16 bits
        wf.setframerate(sample_rate)
        wf.writeframes(recording.tobytes())
    
    print(f"Échantillon vocal enregistré sous {filename}")

# Test d'enregistrement
if __name__ == "__main__":
    if not os.path.exists("data"):
        os.makedirs("data")
    record_voice(filename="data/user_sample.wav", duration=5)
