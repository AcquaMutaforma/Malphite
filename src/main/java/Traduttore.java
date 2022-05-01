import contenitori.APIdiAppoggio;
import contenitori.ElementoAudio;
import contenitori.ElementoTradotto;

/** Classe che prende degli elementi*/
public class Traduttore implements IntTraduttre{

    APIdiAppoggio api;

    public Traduttore(APIdiAppoggio api) {
        this.api = api;
    }

    public ElementoTradotto audioToString(ElementoAudio audio){
        return new ElementoTradotto(audio, this.api.traduciAudio(audio));
    }

    public void setAPIdiAppoggio(APIdiAppoggio api) {
        this.api = api;
    }

}
