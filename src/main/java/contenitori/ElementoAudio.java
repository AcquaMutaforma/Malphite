import javax.sound.sampled.AudioFormat;

public class ElementoAudio {
    int id;
    AudioFormat audio;

    public ElementoAudio(int id, AudioFormat audio) {
        this.id = id;
        this.audio = audio;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public AudioFormat getAudio() {
        return audio;
    }

    public void setAudio(AudioFormat audio) {
        this.audio = audio;
    }
}
