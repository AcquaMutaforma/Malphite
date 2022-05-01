import contenitori.ElementoAudio;

/** Classe per gestione INPUT, crea oggetto audio da tradurre */
public class AudioHandler {

    IDManager idManager;
    int sec;   //secondi in cui ascolta un comando, quindi la grandezza di un blocco da inviare

    public AudioHandler(IDManager idManager, int secondiDurataAudio){
        this.idManager = idManager;
        this.sec = secondiDurataAudio;
    }

    public ElementoAudio getComando(){
        ElementoAudio toreturn = null;
        //TODO
        return toreturn;
    }

}
