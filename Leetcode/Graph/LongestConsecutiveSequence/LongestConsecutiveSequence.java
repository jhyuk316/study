package Graph.LongestConsecutiveSequence;
// 128. Longest Consecutive Sequence
// https://leetcode.com/problems/longest-consecutive-sequence/

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


// O(n) dfs, memoization
class Solution {
    Map<Integer, List<Integer>> graph = new HashMap<>();
    Map<Integer, Integer> memo = new HashMap<>();

    public int longestConsecutive(int[] nums) {
        for (int num : nums) {
            if (graph.containsKey(num - 1)) {
                graph.get(num - 1).add(num);
            } else {
                List<Integer> tempList = new ArrayList<>();
                tempList.add(num);
                graph.put(num - 1, tempList);
            }
        }

        System.out.println(graph);

        int maxDepth = 0;
        for (int num : nums) {
            maxDepth = Math.max(maxDepth, dfs(num));
        }

        System.out.println(memo);
        return maxDepth;
    }

    private int dfs(int node) {
        if (graph.containsKey(node) == false) {
            return 1;
        }
        if (memo.containsKey(node)) {
            return memo.get(node);
        }

        int result = dfs(node + 1) + 1;
        memo.put(node, result);
        return result;
    }
}


public class LongestConsecutiveSequence {
    public static void main(String[] args) {
        testSol(List.of(new int[] {100, 4, 200, 1, 3, 2}), 4);
        testSol(List.of(new int[] {0, 3, 7, 2, 5, 8, 4, 6, 0, 1}), 9);
    }

    static void testSol(List input, Object output) {
        // todo : input, output match
        int[] arg1 = (int[]) input.get(0);
        int out = (int) output;
        Solution sol = new Solution();
        // todo : solution match
        int res = sol.longestConsecutive(arg1);
        if (res == out) {
            System.out.println("O : " + res);
        } else {
            System.out.println("x : " + res + "	expect : " + out);
        }
    }
}
