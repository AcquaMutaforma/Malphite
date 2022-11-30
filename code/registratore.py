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
soglia_y = 800  # soglia audio di sottofondo


# old
def get_audio(duration=4.0) -> str:
    recording = sd.rec(int(duration * frequency), dtype=np.int16)
    sd.wait()  # Wait for the audio to complete
    print(recording.dtype)
    nome_file = __audio_to_file(recording=recording)
    log.logInfo(str('registrato audio: ' + nome_file))
    return nome_file


# old
def __audio_to_file(recording):
    """Trasforma una variabile audio in un file in memoria"""
    return file_handler.audio_to_file(frequency, recording)


def get_audio_stream():
    try:
        return sd.InputStream(samplerate=frequency, channels=1, dtype='int16')  # parte da solo? booh
    except Exception as e:
        log.logError("Errore input stream = {" + str(e) + "}")

