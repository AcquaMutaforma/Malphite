import sounddevice as sd
import soundfile as sf
from . import logManager as log


def riproduci_audio(nome_file: str):
    try:
        data, fs = sf.read(nome_file, dtype='float32')
        sd.play(data, fs)
        sd.wait()  # aspetta la fine della riproduzione
        log.logInfo(f'Riprodotto file audio ["{nome_file}"]')
    except FileNotFoundError as e:  # riproduzione di un messaggio pre-registrato di errore?
        log.logError(f'riproduzione audio ["{nome_file}"] fallita :' + e.strerror)
    except FileExistsError as e:
        log.logError(f'riproduzione audio ["{nome_file}"] fallita :' + e.strerror)


def suonaSveglia():
    riproduci_audio('sveglia.wav')
