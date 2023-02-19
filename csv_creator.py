"""
Script di appoggio per elaborazione file CSV utile al training della rete neurale.

Per comodità registriamo a blocchi la stessa frase, inseriamo nel file CSV i dati dei file audio registrati e la
loro traduzione. In questo modo la fase di testing è più veloce, dato che non si ha la necessità di riascoltare ogni
audio registrato per inserire la sua traduzione manualmente nel file.

Ovviamente i files già inseriti nel file CSV vengono ignorati, così da non sovrascriveli.
Una volta elaborati
"""
import logManager as log
cartella_files = "test_passiva/"


def addLineToCSV(filename: str, grandezza: int, frase: str):
    try:
        f = open(cartella_files + "lista.csv", 'a')
        tmp = filename + "," + str(grandezza) + "," + frase
        f.write(tmp + "\n")
    except Exception as e:
        log.logError(f"{e} - Impossibile modificare il file CSV")
