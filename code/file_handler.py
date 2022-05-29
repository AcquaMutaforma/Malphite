import random
from scipy.io.wavfile import write
import os
import soundfile as sf

cartella_comando = "audio_richieste/"
cartella_risposte = "risposte_registrate/"
info_risposte = cartella_risposte + "/infoRisposte.txt"


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
        print("[File_H] - Errore indefinito - scrittura richiesta fallita :(")
        return None
    return file_audio


def elimina_audio(filename: str):
    """Utilizzato per cancellare le richieste una volta completata la gestione e per la rimozione
    di file audio delle risposte se necessario"""
    if os.path.exists(filename):
        try:
            os.remove(filename)
            print("[File_H] - Audio correttamente rimosso")
        except PermissionError:
            print(f"[File_H] - Errore permessi rimozione file audio ^ {filename} ^")
        except Exception:
            print("[File_H] - Errore indefinito - rimozione audio fallita :(")
    else:
        print(f"[File_H] - Audio da rimuovere non trovato ^{filename}")


def get_mappa_decisore():
    if os.path.exists(info_risposte):
        f = open(info_risposte, 'r')
        toreturn = f.read()
        f.close()
        return toreturn
    else:
        f = open(info_risposte, 'x')
        f.close()
        return ''
        # tanto se il file e' vuoto, al decisore arriva comunque un '' quindi evito di aprire il file


def update_mappa_decisore(str_oggetti_json: str):
    try:
        f = open(info_risposte, 'w')
        f.write(str_oggetti_json)
        f.close()
    except PermissionError:
        print("[File_H] - Errore permessi per aggiornamento mappa")
    except Exception:
        print("[File_H] - Errore indefinito per aggiornamento mappa")
    print("[File_H] - Mappa risposte aggiornata")


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


def add_audio_risposta(nome_file: str, registrazione: str):
    """Inserisce una nuova registrazione nella cartella di risposte registrate dal custode"""
    try:
        destinazione = cartella_risposte + "/" + nome_file
        sorgente = os.fspath(registrazione)
        os.replace(sorgente, destinazione)
    except PermissionError:
        print("[File_H] - Errore permessi per aggiungere/modificare file audio")
    except FileNotFoundError:
        print("[File_H] - File registrazione non trovato")
    except Exception:
        print("[File_H] - Errore indefinito per aggiungere/modificare registrazione :(")
    # todo: controllare che funzioni davvero >.<


def update_audio_risposta(nome_file: str, registrazione: str):
    add_audio_risposta(nome_file, registrazione)
