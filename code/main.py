import registratore as rg
# import coquiManager
# import events_handler todo: da fixare un bel po di cose
import logManager
import connessioneManager as cm
import file_handler as fh
import numpy as np
import time
from datetime import date
import datetime

"""
Modalita attiva e passiva utilizzano una variabile boolean.
Mod passiva chiama solo il metodo dedicato, per registrare e inviare
Mod attiva inizializza tutti i dati e avvia la registrazione, traduzione etc..
---------------------------------------------------------------------
#MOD ATTIVA
Esegue tutte le funzioni, sveglia, traduzione, risposta etc..

load configurazione e event_handler
inizializza coqui con model etc
avvia registratore
---------------------------------------------------------------------
#MOD PASSIVA
Esegue solamente un loop di registrazione e invio degli audio.

avvia registratore
utilizza connessioneManager per inviare gli audio non vuoti
"""

ATTIVA = True
PASSIVA = False
MODALITA = PASSIVA

registratore = rg.get_audio_stream()
MAX_GIRI_VUOTI = 2


def main():
    if MODALITA:
        pass
    else:
        modPassiva()


def modPassiva():
    numero_giri_a_vuoto = 0
    buffer = np.empty(shape=(0, 0))
    while True:
        solo_rumore = True
        tmp = registratore.read(rg.frequency)
        for x in np.nditer(tmp):
            if abs(x) > rg.soglia_y:
                solo_rumore = False
                break
        # se ogni elemento è < di 0.003 allora ignoro il nuovo blocco, scrivo e invio un file audio
        if solo_rumore:
            numero_giri_a_vuoto += 1
        else:
            __aggiungi_al_buffer(buffer, tmp)

        if numero_giri_a_vuoto >= (MAX_GIRI_VUOTI - 1):
            audio = fh.audio_to_file(rg.frequency, buffer)
            cm.invia(audio)
            fh.elimina_audio(audio)
            numero_giri_a_vuoto = 0


def __aggiungi_al_buffer(buffer: np.ndarray, arr: np.ndarray):
    """Creo un nuovo array con il buffer precedente e aggiungo quello nuovo (arr).
     ovviamente seguendo un contatore, che rappresenta i secondi. Il buffer dovrebbe essere
     tagliato a blocchi da 16k in teoria, cosi coqui non deve fare controlli strani, basta inserire
     quel valore come samplerate. Da controllare meglio"""

