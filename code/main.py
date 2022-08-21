"""Si puo' personalizzare il programma modificando i seguenti oggetti:
myapi, registratore, message_handler e output_handler"""
import servizio_AssemblyAI as myapi
import traduttore as trad
import registratore
import decisore
import esecutore
import message_handler
import output_handler

if __name__ == '__main__':

    # ------ Avvio oggetti necessari ------
    traduttore = trad.Traduttore(api=myapi)
    mess_h = message_handler.TeleBot()
    esec = esecutore.Esecutore(messaggistica=mess_h, output=output_handler)
    decisore = decisore.Decisore(esec)

    # ------ Non avevo altre idee, quindi per ora si avvia cosi' ------------------------
    print("Scrivi 'start' per iniziare, altrimenti chiudo")
    comando = input()
    if 'start' in comando:
        registrazione = registratore.get_audio(3.0)
        elem_tradotto = traduttore.traduci(registrazione)
        decisore.valuta_comando(elem_trad=elem_tradotto)
    print("Ok - i'm done")
    exit(0)
