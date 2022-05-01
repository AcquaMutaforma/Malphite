import contenitori.APIdiAppoggio;
import contenitori.ElementoAudio;
import contenitori.ElementoTradotto;

public interface IntTraduttre {

    ElementoTradotto audioToString(ElementoAudio audio);
    void setAPIdiAppoggio(APIdiAppoggio api);

}
