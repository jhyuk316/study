import java.util.*;

public class treeSetTest {
    public static void main(String[] args) {
        Set treeSet = new TreeSet();
        Set hashSet = new HashSet();

        for (int i = 0; hashSet.size() < 6; i++) {
            int num = (int) (Math.random() * 45) + 1;
            hashSet.add(num); // set.add(new Integer(num));
            treeSet.add(num);
        }

        System.out.println("HashSet: " + hashSet);
        System.out.println("TreeSet: " + treeSet);
    }
}
