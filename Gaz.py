import RPi.GPIO as GPIO
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore

# Configuration du GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Définir la broche d'entrée analogique (à adapter selon votre configuration)
ANALOG_PIN = 28

# Configuration de Firebase
cred = credentials.Certificate('/usr/src/app/fir-gaz-firebase-adminsdk-689r5-0eda1b60be.json') # Remplacez par le chemin de votre fichier de clé de compte de service
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://fir-gaz-default-rtdb.firebaseio.com//' 
})


def read_analog(pin):
    """
    Cette fonction lit la valeur analogique du capteur.
    """
    # Ici, nous ne lisons pas vraiment une entrée analogique directement,
    # mais nous simulerons une lecture en retournant une valeur fictive.
    # Vous devez remplacer cela par votre propre code pour lire une entrée analogique directement.

    # Pour cet exemple, nous retournons simplement une valeur fictive
    return 300


try:
    while True:
        # Lecture de la valeur analogique du capteur
        valeur_analogique = read_analog(ANALOG_PIN)

        # Conversion de la valeur analogique en concentration de CO2 (à adapter selon la calibration de votre capteur)
        concentration_co2 = valeur_analogique  # Besoin de calibrer correctement ici

        # Affichage de la valeur
        print("Concentration de CO2: {} ppm".format(concentration_co2))

        # Envoi de la valeur à Firebase
        ref = db.reference('co2_concentration')
        ref.push({
            'timestamp': int(time.time()),
            'concentration': concentration_co2
        })

        # Attente avant la prochaine lecture
        time.sleep(1)
        
except KeyboardInterrupt:
    # Arrêt propre si l'utilisateur appuie sur Ctrl+C
    GPIO.cleanup()
