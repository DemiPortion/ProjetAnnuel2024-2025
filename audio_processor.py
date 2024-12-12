import librosa
import numpy as np
import os

def extract_features(file_path):
    # Charger l'audio
    audio, sample_rate = librosa.load(file_path, sr=16000, mono=True)
    # Extraire les MFCC (Mel Frequency Cepstral Coefficients)
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    return np.mean(mfccs.T, axis=0)

def load_data(data_path):
    X, y = [], []
    for user_dir in os.listdir(data_path):
        user_path = os.path.join(data_path, user_dir)
        if os.path.isdir(user_path):
            for file in os.listdir(user_path):
                file_path = os.path.join(user_path, file)
                if file.endswith('.wav'):
                    features = extract_features(file_path)
                    X.append(features)
                    y.append(user_dir)
    return np.array(X), np.array(y)
