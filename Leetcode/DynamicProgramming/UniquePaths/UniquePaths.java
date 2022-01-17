package DynamicProgramming.UniquePaths;
// 62. Unique Paths
// https://leetcode.com/problems/unique-paths/

import java.util.Arrays;
import java.util.List;


// O(n) tabulation dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
class Solution {
    public int uniquePaths(int m, int n) {
        int[][] dp = new int[m][n];

        Arrays.fill(dp[0], 1);
        for (int i = 1; i < m; ++i) {
            dp[i][0] = 1;
        }

        for (int i = 1; i < m; ++i) {
            for (int j = 1; j < n; ++j) {
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }

        return dp[m - 1][n - 1];
    }
}


// O(n) combination
class Solution1 {
    public int uniquePaths(int m, int n) {
        int num = m + n - 1;
        int combi = Math.min(m, n) - 1;

        double result = 1;
        for (int i = 1; i < combi + 1; ++i) {
            result *= num - i;
            result /= i;
        }

        return (int) result;
    }
}


public class UniquePaths {
    public static void main(String[] args) {
        testSol(List.of(3, 7), 28);
        testSol(List.of(3, 2), 3);
        testSol(List.of(8, 20), 657800);
        testSol(List.of(15, 19), 471435600);
    }

    static void testSol(List input, Object output) {
        // todo : input, output match
        int arg1 = (int) input.get(0);
        int arg2 = (int) input.get(1);
        int out = (int) output;
        Solution sol = new Solution();
        // todo : solution match
        int res = sol.uniquePaths(arg1, arg2);
        if (res == out) {
            System.out.println("O : " + res);
        } else {
            System.out.println("x : " + res + "	expect : " + out);
        }
    }


}
