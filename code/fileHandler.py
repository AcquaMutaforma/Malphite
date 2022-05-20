import random
from scipy.io.wavfile import write

cartella_comando = "audio_richieste/"


def crea_file_richiesta(freq, recording):
    """Questo metodo scrive la registrazione nella cartella_comando, se e' gia' presente un file
    con lo stesso nome lo sovrascrive. Tecnicamente i comandi vengono gestiti singolarmente, ma nel
    dubbio i file vengono chiamati in maniera differente con un numero random. """
    file_audio = cartella_comando + "richiesta" + str(random.randrange(0, 20)) + ".wav"
    try:
        write(file_audio, freq, recording)
    except PermissionError:
        print(f"[File_H] - Errore permessi scrittura file in ^ {cartella_comando} ^")
        return None
    except FileNotFoundError:
        print(f"[File_H] - Errore file not found - {cartella_comando} -or- {recording.__class__}")
        return None
    except Exception:
        print("[File_H] - Errore indefinito - crea_file_richiesta()")
        return None
    return file_audio


def elimina_audio_processato(filename):
    pass  # todo


def get_mappa_decisore(todo):
    pass  # todo


def update_mappa_decisore(todo):
    pass  # todo


def get_audio_risposta(nome_file):
    """Recupera la registrazione di una risposta, se non viene trovata genera un errore"""
    pass


def add_audio_risposta(registrazione):
    """Inserisce una nuova registrazione nella cartella di risposte registrate dal custode"""
    pass  # todo


'''
Le funzioni seguenti sono secondarie, da fare con calma
'''


def update_audio_risposta(todo):
    pass  # todo


def elimina_audio_risposta(todo):
    pass  # todo
