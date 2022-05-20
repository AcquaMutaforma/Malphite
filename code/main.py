""" Main del sistema, inizializza gli oggetti necessari al funzionamento """

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import servizio_AssemblyAI
import traduttore as trad
import registratore


if __name__ == '__main__':

    traduttore = trad.Traduttore(api=servizio_AssemblyAI)

# ------ Non avevo altre idee, quindi per ora si avvia cosi' ------------------------
    print("Scrivi 'start' per iniziare, altrimenti chiudo")
    comando = input()
    if 'start' in comando:
        registrazione = registratore.get_audio(3.0)
        elem_tradotto = traduttore.traduci(registrazione)
    else:
        print("Ok - i'm done")
    exit(0)
