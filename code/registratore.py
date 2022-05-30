""" Classe che gestisce l'input audio
Responsabilita' :
Catturare audio in input
Definire durata dell'audio
"""

import sounddevice as sd
import file_handler

"""
For repeated use you can set defaults using default:
sd.default.samplerate = frequency
sd.default.channels = 2

After that, you can drop the additional arguments:
myrecording = sd.rec(int(duration * frequency))

"""
frequency = 44400  # Sampling frequency
sd.default.samplerate = frequency
sd.default.channels = 2


def get_audio(secondi):
    if secondi is None:
        duration = 4.0  # Recording duration in seconds
    else:
        duration = secondi
    # to record audio from sound-device into a Numpy
    # recording = sd.rec(int(duration * frequency), samplerate=frequency, channels=2)
    print("[Registratore] - avvio registrazione ")
    recording = sd.rec(int(duration * frequency))
    sd.wait()  # Wait for the audio to complete
    print("[Registratore] - registrazione completata!")

    # using scipy to save the recording in .wav format
    # This will convert the NumPy array to an audio file with the given sampling frequency
    nome_file = __audio_to_file(recording=recording)
    print(f"[audio_H] - Registrazione = {nome_file}")
    return nome_file  # Restituisco il nome, poi il traduttore lo usa.
    # In alternativa possiamo chiamare da qua il traduttore, da valutare todo..


def __audio_to_file(recording):
    return file_handler.crea_file_richiesta(frequency, recording)
