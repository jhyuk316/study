package String.LongestPalindromicSubstring;
// 5. Longest Palindromic Substring
// https://leetcode.com/problems/longest-palindromic-substring/

import java.util.List;

// O(n^2)
class Solution {
    public String longestPalindrome(String s) {
        String reverseS = new StringBuffer(s).reverse().toString();
        if (s.length() <= 1 || s.equals(reverseS)) { // 숏컷이 너무 빠름.
            return s;
        }

        String maxPal = s.substring(0, 1);

        for (int i = 0; i < s.length() - 1; ++i) {
            String odd = maxPalindrome(s, i, i);
            String even = maxPalindrome(s, i, i + 1);

            String tempPal = odd.length() > even.length() ? odd : even;

            if (maxPal.length() < tempPal.length()) {
                maxPal = tempPal;
            }
        }

        return maxPal;
    }

    private String maxPalindrome(String s, int left, int right) {
        while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
            --left;
            right++;
        }
        return s.substring(left + 1, right);
    }
}


// O(m*n^2) : n : length of s, m : maxLength
class Solution1 {
    public String longestPalindrome(String s) {
        int maxLen = 1;
        int start = 0;

        for (int i = 1; i < s.length(); ++i) {
            if (i - maxLen >= 0) {
                String even = s.substring(i - maxLen, i + 1);
                String reverseEven = new StringBuffer(even).reverse().toString();
                if (i - maxLen >= 0 && even.equals(reverseEven)) {
                    start = i - maxLen;
                    maxLen += 1;
                }
            }
            if (i - maxLen - 1 >= 0) {
                String odd = s.substring(i - maxLen - 1, i + 1);
                String reverseOdd = new StringBuffer(odd).reverse().toString();
                if (odd.equals(reverseOdd)) {
                    start = i - maxLen - 1;
                    maxLen += 2;
                }
            }
        }

        return s.substring(start, start + maxLen);
    }
}


public class LongestPalindromicSubstring {
    public static void main(String[] args) {
        testSol(List.of("ab"), "a");
        testSol(List.of("bb"), "bb");
        testSol(List.of("babad"), "bab");
        testSol(List.of("cbbd"), "bb");
        testSol(List.of("abckcba"), "abckcba");
        testSol(List.of("aaaaaaaaaaa"), "aaaaaaaaaaa");
    }

    static void testSol(List input, Object output) {
        // todo : input, output match
        String arg1 = (String) input.get(0);
        String out = (String) output;

        Solution sol = new Solution();
        // todo : solution match
        String res = sol.longestPalindrome(arg1);

        if (res.equals(out)) {
            System.out.println("O : " + res);
        } else {
            System.out.println("x : " + res + "	expect : " + out);
        }
    }
}
