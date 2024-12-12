import os
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from joblib import dump, load
from audio_processor import extract_features

def train_model(data_folder="data", model_path="voice_model.joblib"):
    """
    Entraîne un modèle KNN sur des échantillons vocaux.
    """
    X = []
    y = []

    for label in os.listdir(data_folder):
        label_path = os.path.join(data_folder, label)
        if os.path.isdir(label_path):
            for file in os.listdir(label_path):
                if file.endswith(".wav"):
                    file_path = os.path.join(label_path, file)
                    features = extract_features(file_path)
                    X.append(features)
                    y.append(label)
    
    # Entraînement du modèle KNN
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(X, y)
    
    # Sauvegarde du modèle
    dump(knn, model_path)
    print(f"Modèle sauvegardé sous {model_path}")

# Test d'entraînement
if __name__ == "__main__":
    train_model()
