import sounddevice as sd
import file_handler
import logManager as log


def riproduci_audio(nome_file: str):
    # Vengono forniti 2 input, controllare se funziona bene
    #  print("[Output_H] - Riproduzione file audio")
    try:
        file = file_handler.apri_audio_risposta(nome_file)
        sd.play(file)
        sd.wait()  # aspetta la fine della riproduzione
        file.close()
        #  print("[Output_H] - Riproduzione file completata")
    except FileNotFoundError:  #  riproduzione di un messaggio pre-registrato di errore?
        log.logError('output_handler - FILE NOT FOUND ERROR -')
