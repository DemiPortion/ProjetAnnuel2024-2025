import numpy as np
import librosa

def extract_features(file_path, n_mfcc=13):
    """
    Extrait des caractéristiques MFCC à partir d'un fichier audio.
    """
    y, sr = librosa.load(file_path, sr=None)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    mfcc_mean = np.mean(mfcc.T, axis=0)  # Moyenne des coefficients
    return mfcc_mean

# Test de traitement
if __name__ == "__main__":
    features = extract_features("data/user_sample.wav")
    print("Caractéristiques audio extraites :")
    print(features)
