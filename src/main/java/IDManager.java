public class IDManager {
    int lastID;

    public IDManager(){
        this.lastID = 0;
    }

    public int generateNewId(){
        this.lastID++;
        return this.lastID;
    }
}
