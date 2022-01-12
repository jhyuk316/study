package DynamicProgramming.WordBreak;
// 139. Word Break
// https://leetcode.com/problems/word-break/

import java.util.Arrays;
import java.util.List;

// O(n*m), n : length of s, m : size of wordDict
class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        boolean[] result = new boolean[s.length() + 1];
        result[s.length()] = true;

        for (int i = s.length(); i >= 0; --i) {
            for (String word : wordDict) {
                int endIndex = i + word.length();
                if (endIndex > s.length()) {
                    continue;
                }

                if (result[endIndex] == true && s.substring(i, endIndex).equals(word)) {
                    result[i] = result[endIndex];
                    break;
                }
            }
        }

        System.out.println(Arrays.toString(result));
        return result[0];
    }
}


public class WordBreak {
    public static void main(String[] args) {
        testSol(List.of("leetcode", List.of("leet", "code")), true);
        testSol(List.of("applepenapple", List.of("apple", "pen")), true);
        testSol(List.of("catsandog", List.of("cats", "dog", "sand", "and", "cat")), false);
    }

    static void testSol(List input, Object output) {
        String input1 = (String) input.get(0);
        List<String> input2 = (List<String>) input.get(1);
        boolean out = (boolean) output;

        Solution sol = new Solution();
        boolean res = sol.wordBreak(input1, input2);

        if (res == out) {
            System.out.println("O : " + res);
        } else {
            System.out.println("x : " + res + "\texpect : " + out);
        }
    }
}
