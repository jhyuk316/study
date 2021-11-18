public class Oop {
    public static void main(String[] args) {
        TV[] tvList = new TV[3];
        
        tvList[0] = new TV();
        System.out.println(tvList[0].channel);


        
    }
    
}

class TV{
    String color;
    boolean power;
    public int channel;

    void power() {power = !power;}
    void channelUp() { ++channel;}
    void channelDown() { --channel;}
}
