/*
    Classe improvvisata per test iniziali sul funzionamento API per traduzione audio testo e viceversa
 */
public class TestContainer_API {

    public static void main(String[] args) {
        Ascoltatore a = new Ascoltatore();
        IntTraduttre t = new Traduttore();

        String comando = t.audioToString(a.getComando());
        System.out.println("\nComando input :"+comando);
        System.out.println("\nFine\n");
    }



}
