package Binary.CountingBits;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

// O(n)
class Solution {
    public int[] countBits(int n) {
        int[] result = new int[n + 1];
        for (int i = 1; i < n + 1; ++i) {
            result[i] = result[i >> 1] + (i & 1);
        }
        // System.out.println(Arrays.toString(result));
        return result;
    }
}


// O(n^2)
class Solution1 {
    public int[] countBits(int n) {
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i <= n; ++i) {
            list.add(_countBits(i));
        }

        int[] result = new int[list.size()];

        for (int i = 0; i < list.size(); ++i) {
            result[i] = list.get(i);
        }

        // System.out.println(Arrays.toString(result));
        return result;
    }

    public int _countBits(int n) {
        int count = 0;
        while (n != 0) {
            if ((n & 1) == 1) {
                count++;
            }
            n = n >>> 1;
        }
        return count;
    }
}


public class CountingBits {
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.countBits(0));
        System.out.println(sol.countBits(5));
        System.out.println(sol.countBits(32));
    }

}
