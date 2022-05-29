import sounddevice as sd
import file_handler


def riproduci_audio(nome_file: str):
    # Vengono forniti 2 input, controllare se funziona bene
    print("[Output_H] - Riproduzione file audio")
    sd.play(file_handler.apri_audio_risposta(nome_file))
    sd.wait()  # aspetta la fine della riproduzione
    print("[Output_H] - Riproduzione file completata")
