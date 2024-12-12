from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from joblib import dump
import audio_processor

def train_model():
    # Charger les données
    X, y = audio_processor.load_data("data/")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entraîner un modèle SVM
    model = SVC(kernel='linear', probability=True)
    model.fit(X_train, y_train)

    # Évaluer le modèle
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

    # Sauvegarder le modèle
    dump(model, "voice_model.joblib")
    print("Model saved to voice_model.joblib")

if __name__ == "__main__":
    train_model()
