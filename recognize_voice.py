from joblib import load
from audio_processor import extract_features
from voice_recorder import record_voice

def recognize_voice(model_path="voice_model.joblib", temp_file="temp.wav"):
    """
    Reconnaît la voix en comparant avec le modèle existant.
    """
    record_voice(filename=temp_file, duration=5)
    features = extract_features(temp_file)
    knn = load(model_path)
    prediction = knn.predict([features])
    print(f"Voix reconnue comme : {prediction[0]}")

# Test de reconnaissance
if __name__ == "__main__":
    recognize_voice()
