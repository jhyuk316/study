import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

/**
 * DiningPhilosophers. 미완성, 작성중..
 * 
 * 식사하는 철학자 문제 모니터를 이용한 해결.
 * 
 * 해결책 - 양 쪽의 젓가락이 모두 놓여있으면 식사.
 */

public class DiningPhilosophers {
    enum State {
        THINKING, HUNGRY, EATING
    };

    public State[] state = new State[5]; // 철학자

    private final Lock lock = new ReentrantLock();
    List<Condition> selfCondi = new ArrayList<>();

    DiningPhilosophers() {
        for (int i = 0; i < 5; i++) {
            this.selfCondi.add(lock.newCondition());
            state[i] = State.THINKING;
        }
    }

    void pickup(int i) { // Acquires
        lock.lock();
        state[i] = State.HUNGRY;
        test(i);
        if (state[i] != State.EATING) {
            try {
                this.selfCondi.get(i).await();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        lock.unlock();
    }

    void putdown(int i) { // Releases
        state[i] = State.THINKING;
        test((i + 4) % 5); // left
        test((i + 1) % 5); // right
    }

    void test(int i) {
        lock.lock();
        if ((state[(i + 4) % 5] != State.EATING) && (state[i] == State.HUNGRY)
                && (state[(i + 1) % 5] != State.EATING)) {
            state[i] = State.EATING;
            this.selfCondi.get(i).signal();
        }
        lock.unlock();
    }

    public static void main(String[] args) {
        DiningPhilosophers dp = new DiningPhilosophers();

        dp.pickup(1);
        dp.printState();
        // dp.pickup(2);
        // dp.printState();
        // dp.pickup(3);
        // dp.printState();
        // dp.pickup(4);
        // dp.printState();
        // dp.pickup(5);
        // dp.printState();
    }

    void printState() {
        for (int i = 0; i < 5; ++i) {
            System.out.print(i + ":" + state[i] + " ");
        }
    }
}
