from joblib import load
import audio_processor
import voice_recorder

def recognize_user():
    # Charger le modèle
    model = load("voice_model.joblib")
    
    # Enregistrer un fichier audio
    print("Recording for recognition...")
    voice_recorder.record_audio("temp.wav")
    
    # Extraire les caractéristiques
    features = audio_processor.extract_features("temp.wav")
    
    # Prédire l'utilisateur
    prediction = model.predict([features])
    probabilities = model.predict_proba([features])
    confidence = max(probabilities[0]) * 100
    
    print(f"Recognized User: {prediction[0]} with {confidence:.2f}% confidence.")
    os.remove("temp.wav")  # Supprimer le fichier temporaire

if __name__ == "__main__":
    recognize_user()
