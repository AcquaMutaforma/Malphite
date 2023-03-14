import sounddevice as sd
import mysite.Malphite.logManager as log
from mysite.Malphite import file_handler


def riproduci_audio(nome_file: str):
    try:
        file = file_handler.apri_audio_risposta(nome_file)
        sd.play(file)
        sd.wait()  # aspetta la fine della riproduzione
        file.close()
        log.logInfo(f'Riprodotto file audio ["{nome_file}"]')
    except FileNotFoundError as e:  # riproduzione di un messaggio pre-registrato di errore?
        log.logError(f'riproduzione audio ["{nome_file}"] fallita :' + e.strerror)
    except FileExistsError as e:
        log.logError(f'riproduzione audio ["{nome_file}"] fallita :' + e.strerror)


def suonaSveglia():
    riproduci_audio('sveglia.wav')
