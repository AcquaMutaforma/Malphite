package contenitori;

public class ElementoTradotto {

    ElementoAudio elementoAudio;
    String traduzione;

    public ElementoTradotto(ElementoAudio elementoAudio, String traduzione) {
        this.elementoAudio = elementoAudio;
        this.traduzione = traduzione;
    }

    public int getID(){
        return elementoAudio.getId();
    }

    //Generati

    public ElementoAudio getElementoAudio() {
        return elementoAudio;
    }

    public void setElementoAudio(ElementoAudio elementoAudio) {
        this.elementoAudio = elementoAudio;
    }

    public String getTraduzione() {
        return traduzione;
    }

    public void setTraduzione(String traduzione) {
        this.traduzione = traduzione;
    }
}
