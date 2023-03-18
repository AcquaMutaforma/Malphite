import playsound
import mysite.Malphite.logManager as log


def riproduci_audio(nome_file: str):
    try:
        playsound.playsound(nome_file)
        log.logInfo(f'Riprodotto file audio ["{nome_file}"]')
    except FileNotFoundError as e:  # riproduzione di un messaggio pre-registrato di errore?
        log.logError(f'riproduzione audio ["{nome_file}"] fallita :' + e.strerror)
    except FileExistsError as e:
        log.logError(f'riproduzione audio ["{nome_file}"] fallita :' + e.strerror)


def suonaSveglia():
    riproduci_audio('sveglia.wav')
