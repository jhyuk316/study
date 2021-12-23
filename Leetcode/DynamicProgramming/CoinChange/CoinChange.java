package DynamicProgramming.CoinChange;
// 322. Coin Change
// https://leetcode.com/problems/coin-change/

import java.util.Arrays;

// O(m*n)
class Solution {
    public int coinChange(int[] coins, int amount) {
        if (amount == 0) {
            return 0;
        }

        int[] count = new int[amount + 1];

        for (int i = 1; i < count.length; ++i) {
            for (int j = 0; j < coins.length; ++j) {
                if (i < coins[j]) {
                    continue;
                } else if (i == coins[j]) {
                    count[i] = 1;
                }

                if (count[i - coins[j]] > 0) {
                    if (count[i] == 0)
                        count[i] = count[i - coins[j]] + 1;

                    count[i] = Math.min(count[i], count[i - coins[j]] + 1);
                }
            }

        }

        System.out.println(Arrays.toString(count));
        return count[amount] == 0 ? -1 : count[amount];
    }
}


public class CoinChange {
    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.coinChange(new int[] {1, 2, 5}, 11));
        // System.out.println(sol.coinChange(new int[] {5}, 11));
        // System.out.println(sol.coinChange(new int[] {}, 11));
        // System.out.println(sol.coinChange(new int[] {}, 0));
        // System.out.println(sol.coinChange(new int[] {2}, 1));

        // System.out.println(sol.coinChange(new int[] {1, 2, 5}, 101));
        // System.out.println(sol.coinChange(new int[] {1, 7, 12}, 14));
        // System.out.println(sol.coinChange(new int[] {7, 11}, 36));
        // System.out.println(sol.coinChange(new int[] {186, 419, 83, 408}, 6249));
    }

}
