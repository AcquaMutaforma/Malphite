import time
from . import logManager as log
from datetime import date
import os
import soundfile as sf

cartella_registrazioni = "modPassiva/"
cartella_risposte = "risposte_registrate/"


def audio_to_file(freq, recording):
    """Questo metodo scrive la registrazione nella cartella_comando, se e' gia' presente un file
    con lo stesso nome lo sovrascrive. Tecnicamente i comandi vengono gestiti singolarmente, ma nel
    dubbio i file vengono chiamati in maniera differente con un numero random. """
    filename = "rec" + date.today().strftime("_%d_%m_%y_") + time.strftime("%H_%M_%S", time.localtime()) + ".wav"
    if recording is None or freq < 10000:
        log.logError("Scrittura file fallita, recording = None")
        return 'None'
    try:
        sf.write(file=cartella_registrazioni + filename, samplerate=freq, data=recording)
        print("[File_H] - File audio di richiesta creato correttamente")
    except PermissionError:
        print(f"[File_H] - Errore permessi scrittura file in ^ {cartella_registrazioni} ^")
        return None
    except FileNotFoundError:
        print(f"[File_H] - Errore file not found - {cartella_registrazioni} -or- {recording.__class__}")
        return None
    except Exception as e:
        print(f"[File_H] - scrittura richiesta fallita - {e}")
        return None
    return filename


def elimina_audio(filename: str):
    """Utilizzato per cancellare le richieste una volta completata la gestione e per la rimozione
    di file audio delle risposte se necessario"""
    try:
        os.remove(filename)
        print("[File_H] - Audio correttamente rimosso")
    except FileNotFoundError:
        print(f"[File_H] - Audio da rimuovere non trovato ^{filename}")
    except PermissionError:
        print(f"[File_H] - Errore permessi rimozione file audio ^ {filename} ^")
    except Exception:
        print("[File_H] - Errore indefinito - rimozione audio fallita :(")


def apri_audio_risposta(nome_file: str):
    """Recupera la registrazione di una risposta"""
    try:
        return sf.read(nome_file, dtype='float32')
    except PermissionError:
        print("[File_H] - Errore permessi per aprire file audio")
    except FileNotFoundError:
        print("[File_H] - File audio non trovato")
    except Exception:
        print("[File_H] - Errore indefinito in apertura audio :(")
    return None
