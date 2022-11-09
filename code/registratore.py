"""
Classe che gestisce l'input audio
Responsabilita' :
Catturare audio in input
"""

import sounddevice as sd
import file_handler
import logManager as log
import numpy as np

"""
For repeated use you can set defaults using default:
sd.default.samplerate = frequency
sd.default.channels = 2

After that, you can drop the additional arguments:
myrecording = sd.rec(int(duration * frequency))
"""
frequency = 16000  # Sampling frequency = frequenza campionamento
sd.default.samplerate = frequency
sd.default.channels = 1
soglia_y = 0.003  # soglia audio di sottofondo


def get_audio(duration=4.0) -> str:  # old
    recording = sd.rec(int(duration * frequency), dtype='int16')
    sd.wait()  # Wait for the audio to complete
    print(recording.dtype)
    nome_file = __audio_to_file(recording=recording)
    log.logInfo(str('registrato audio: ' + nome_file))
    return nome_file


def __audio_to_file(recording):  # old
    """Trasforma una variabile audio in un file in memoria"""
    return file_handler.audio_to_file(frequency, recording)


def get_audio_stream():
    try:
        return sd.InputStream(samplerate=frequency, channels=1, dtype='int16')  # parte da solo? booh
    except Exception as e:
        log.logError("Errore input stream = {" + str(e) + "}")


# todo: da cancellare
def crea_audio_da_block(secondi):
    tmp = np.ndarray(shape=(1, 1), dtype='int16')
    valutazione = False
    for i in range(secondi * frequency):
        # recupero i frames per X secondi, e ci faccio un file audio se contiene qualcosa
        tmp.put()
    for x in tmp:
        if abs(x) > soglia_y:
            valutazione = True
            break
    if valutazione:
        file_handler.audio_to_file(frequency, tmp)

    """
        Se tmp contiene parole (quindi numeri maggiori di +/- 0,004 credo q.q) allora:
        lo aggiungo a blocco, sennò lo skippo.
        Se il blocco è grande almeno 4 secondi (da richiedere in input) allora lo salvo
        come un file e svuoto il buffer.
        """
    pass
