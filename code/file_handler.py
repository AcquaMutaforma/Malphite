import json
import random

from Tools.scripts.ndiff import fopen
from scipy.io.wavfile import write
import os
import soundfile as sf

cartella_comando = "audio_richieste/"
cartella_risposte = "risposte_registrate/"


def crea_file_richiesta(freq, recording):
    """Questo metodo scrive la registrazione nella cartella_comando, se e' gia' presente un file
    con lo stesso nome lo sovrascrive. Tecnicamente i comandi vengono gestiti singolarmente, ma nel
    dubbio i file vengono chiamati in maniera differente con un numero random. """
    file_audio = cartella_comando + "richiesta" + str(random.randrange(0, 20)) + ".wav"
    try:
        write(file_audio, freq, recording)
        print("[File_H] - File audio di richiesta creato correttamente")
    except PermissionError:
        print(f"[File_H] - Errore permessi scrittura file in ^ {cartella_comando} ^")
        return None
    except FileNotFoundError:
        print(f"[File_H] - Errore file not found - {cartella_comando} -or- {recording.__class__}")
        return None
    except Exception:
        print("[File_H] - Errore indefinito - scrittura richiesta fallita :(")
        return None
    return file_audio


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


def add_audio_risposta(nuovo_nome: str, registrazione: str):
    """SPOSTA una nuova registrazione nella cartella di risposte registrate dall'addetto"""
    try:
        destinazione = cartella_risposte + "/" + nuovo_nome
        sorgente = os.fspath(registrazione)
        os.replace(sorgente, destinazione)
        print("[File_H] - Registrazione risposta aggiunta correttamente")
    except PermissionError:
        print("[File_H] - Errore permessi per aggiungere/modificare file audio")
    except FileNotFoundError:
        print("[File_H] - File registrazione non trovato")
    except Exception:
        print("[File_H] - Errore indefinito per aggiungere/modificare registrazione :(")
    # todo: controllare che funzioni davvero >.<


def modifica_audio_risposta(nome_file: str, registrazione: str):
    add_audio_risposta(nome_file, registrazione)


def leggi_config() -> {}:
    f = fopen("config.txt")
    to_ret = json.load(f)
    f.close()
    return to_ret


def scrivi_config(conf: dict):
    f = fopen("config.txt")
    f.write(conf)
    f.close()
