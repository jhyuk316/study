package DynamicProgramming.MinimumASCIIDeleteSumForTwoStrings;
// 712. Minimum ASCII Delete Sum for Two Strings
// https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

import java.util.List;

// O(n^2)
// dp[i][j] = d[i][j-1] + ord(c) if c1 = c2
// dp[i][j] = max(dp[i][j-1], dp[i-1][j]) if c1 != c2
class Solution {
    public int minimumDeleteSum(String s1, String s2) {
        char[] c1 = s1.toCharArray();
        char[] c2 = s2.toCharArray();

        int sum = 0;
        for (char c : c1) {
            sum += c;
        }
        for (char c : c2) {
            sum += c;
        }

        int[][] dp = new int[s1.length() + 1][s2.length() + 1];
        for (int i = 1; i <= s1.length(); ++i) {
            for (int j = 1; j <= s2.length(); ++j) {
                if (c1[i - 1] == c2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + c1[i - 1];
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }

        return sum - dp[s1.length()][s2.length()] * 2;
    }
}


public class MinimumASCIIDeleteSumForTwoStrings {
    public static void main(String[] args) {
        testSol(List.of("delete", "leet"), 403);
        testSol(List.of("zzzzzaaaaaa", "azazazazaza"), 970);
    }

    static void testSol(List input, Object output) {
        // todo : input, output match
        String arg1 = (String) input.get(0);
        String arg2 = (String) input.get(1);
        int out = (int) output;
        Solution sol = new Solution();
        // todo : solution match
        int res = sol.minimumDeleteSum(arg1, arg2);
        if (res == out) {
            System.out.println("O : " + res);
        } else {
            System.out.println("x : " + res + "	expect : " + out);
        }
    }


}

