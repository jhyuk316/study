/**
 * javaThread
 */
public class javaThread extends Thread {
    // public class javaThread implements Runnable {
    int n;
    public static int sum = 0;

    public javaThread(int n) {
        this.n = n;
    }

    public void run() {
        System.out.println(this.n + " thread start.");
        for (int i = 1; i <= this.n; ++i) {
            System.out.println(i);
            sum += i;
        }
        System.out.println(this.n + " thread end.");
    }

    public static void main(String[] args) {
        Thread t = new javaThread(10);
        // Thread t = new Thread(new javaThread(10));
        t.start();
        try {
            t.join();
        } catch (Exception e) {

        }
        System.out.println("Sum = " + sum);
        System.out.println("main end.");
    }
}
