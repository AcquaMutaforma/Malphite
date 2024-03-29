"""
Modulo che gestisce l'input audio
"""
import sounddevice as sd
import logManager as log
import file_handler
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
soglia_y = 800  # soglia rumore, i valori più bassi non sono una persona che parla
'''TODO il valore cambia da dispositivo ad un'altro, e' consigliabile ricalibrarlo togliendo la parte commentata 
nella mod passiva.'''


# version 1
def get_audio(duration=4.0, filename=None) -> str:
    recording = sd.rec(int(duration * frequency), dtype=np.int16)
    sd.wait()  # Wait for the audio to complete
    print(recording.dtype)
    fn = file_handler.audio_to_file(frequency, recording, filename=filename)
    log.logInfo(str('registrato audio: ' + fn))
    return fn


def get_audio_stream():
    try:
        return sd.InputStream(samplerate=frequency, channels=1, dtype='int16')  # parte da solo? booh
    except Exception as e:
        log.logError("Errore input stream = {" + str(e) + "}")
