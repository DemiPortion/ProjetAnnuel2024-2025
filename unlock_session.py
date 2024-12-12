import os
import pyautogui
from recognize_voice import recognize_user

def unlock_session():
    print("Starting voice recognition...")
    recognized_user = recognize_user()  # Appelle la fonction de reconnaissance vocale

    # Définir le mot de passe pour chaque utilisateur (à personnaliser)
    user_passwords = {
        "user1": "password1",  # Remplace par le mot de passe de la session
        "user2": "password2",  # Mot de passe pour user2
    }

    if recognized_user in user_passwords:
        print(f"Recognized User: {recognized_user}. Unlocking session...")
        password = user_passwords[recognized_user]

        # Simule la saisie du mot de passe pour déverrouiller
        pyautogui.typewrite(password)  # Tape le mot de passe
        pyautogui.press("enter")  # Appuie sur "Entrée" pour déverrouiller
    else:
        print("User not recognized or unauthorized.")

if __name__ == "__main__":
    unlock_session()
