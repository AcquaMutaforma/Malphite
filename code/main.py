""" Main del sistema, inizializza gli oggetti necessari al funzionamento """

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# print(f'Hi, {name}')
import servizio_AssemblyAI
import traduttore


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filename = "C:\\Users\\Aley\\Desktop\\Registrazione.m4a"
    # Il traduttore viene inizializzato qua, cosi' quando si vuole modificare il codice basta cambiare qui
    traduttore = traduttore.Traduttore(api=servizio_AssemblyAI.ServizioAai())
    testo = traduttore.traduci(filename)
    print(f"Testo tradotto = {testo}")
