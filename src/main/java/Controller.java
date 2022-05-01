import contenitori.APIdiAppoggio;

public class Controller {

    IDManager idManager = new IDManager();
    AudioHandler audioHandler;
    Traduttore traduttore;
    APIdiAppoggio apiDiAppoggio;

    private boolean creaAudioHandler(int secondiDurataAudio){
        if(secondiDurataAudio < 0 || secondiDurataAudio >14)
            return false;
        this.audioHandler = new AudioHandler(this.idManager, secondiDurataAudio);
        return true;
    }

    private void utilizzaAPIWatson(){
        this.apiDiAppoggio = new APIdiAppoggio(/* todo */);
    }

}
