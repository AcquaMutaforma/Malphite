import time
import logManager as log
from datetime import date
import os
import soundfile as sf

cartella_registrazioni = "modPassiva/"
cartella_risposte = "risposte_registrate/"


def audio_to_file(freq, recording, filename=None):
    """Questo metodo scrive la registrazione nella cartella_comando, se e' gia' presente un file
    con lo stesso nome lo sovrascrive. Tecnicamente i comandi vengono gestiti singolarmente, ma nel
    dubbio i file vengono chiamati in maniera differente con un numero random. """
    if filename is None:
        filename = "rec" + \
                   date.today().strftime("_%d_%m_%y_") + time.strftime("%H_%M_%S", time.localtime()) + ".wav"
    if recording is None or freq < 10000:
        log.logError("Scrittura file fallita, recording = None")
        return 'None'
    filename = cartella_registrazioni + filename
    try:
        sf.write(file=filename, samplerate=freq, data=recording)
        log.logDebug("[File_H] - File audio di richiesta creato correttamente")
    except PermissionError:
        log.logError(f"[File_H] - Errore permessi scrittura file in ^ {cartella_registrazioni} ^")
        return None
    except FileNotFoundError:
        log.logError(f"[File_H] - Errore file not found - {cartella_registrazioni} -or- {recording.__class__}")
        return None
    except Exception as e:
        log.logError(f"[File_H] - Errore indefinito - scrittura richiesta fallita - {e}")
        return None
    return filename


def elimina_audio(filename: str):
    """Utilizzato per cancellare le richieste una volta completata la gestione e per la rimozione
    di file audio delle risposte se necessario"""
    try:
        os.remove(filename)
        log.logDebug("[File_H] - Audio correttamente rimosso")
    except FileNotFoundError:
        log.logError(f"[File_H] - Audio da rimuovere non trovato ^{filename}")
    except PermissionError:
        log.logError(f"[File_H] - Errore permessi rimozione file audio ^ {filename} ^")
    except Exception:
        log.logError("[File_H] - Errore indefinito - rimozione audio fallita :(")
