""" Main del sistema, inizializza gli oggetti necessari al funzionamento """

# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# print(f'Hi, {name}')
import servizio_AssemblyAI


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filename = "C:\\Users\\Aley\\Desktop\\Registrazione.m4a"
    api = servizio_AssemblyAI.servizioAai()
    api.traduzione(filename)
