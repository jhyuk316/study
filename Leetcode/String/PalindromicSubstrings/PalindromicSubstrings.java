package String.PalindromicSubstrings;
// 647. Palindromic Substrings
// https://leetcode.com/problems/palindromic-substrings/

import java.util.List;

// O(n)
class Solution {
    String s;

    public int countSubstrings(String s) {
        this.s = s;

        int sum = 0;
        for (int i = 0; i < s.length(); ++i) {
            sum += countPalindromic(i, i);
            sum += countPalindromic(i, i + 1);
        }

        return sum;
    }

    private int countPalindromic(int s1, int s2) {
        int count = 0;

        while (s1 - count >= 0 && s2 + count < this.s.length()
                && this.s.charAt(s1 - count) == this.s.charAt(s2 + count)) {
            count++;
        }

        return count;
    }
}


public class PalindromicSubstrings {
    public static void main(String[] args) {
        testSol(List.of("abc"), 3);
        testSol(List.of("aaa"), 6);
    }

    static void testSol(List input, Object output) {
        // todo : input, output match
        String arg1 = (String) input.get(0);
        int out = (int) output;
        Solution sol = new Solution();
        // todo : solution match
        int res = sol.countSubstrings(arg1);
        if (res == out) {
            System.out.println("O : " + res);
        } else {
            System.out.println("x : " + res + "	expect : " + out);
        }
    }
}
