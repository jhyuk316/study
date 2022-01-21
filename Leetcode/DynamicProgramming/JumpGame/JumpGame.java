package DynamicProgramming.JumpGame;
// 55. Jump Game
// https://leetcode.com/problems/jump-game/

import java.util.Arrays;
import java.util.List;

// O(n) n:length of nums, 도달 가능한 포인트 표시
class Solution {
    public boolean canJump(int[] nums) {
        int reachPos = nums.length - 1;

        for (int i = nums.length - 2; i >= 0; --i) {
            if (i + nums[i] >= reachPos) {
                reachPos = i;
            }
        }

        if (reachPos != 0) {
            return false;
        }
        return true;
    }
}


// O(n*m) n:length of nums, m: max(nums)
// dp[i] |= dp[i+j], j : 0 <= j <= nums[i]
class Solution1 {
    public boolean canJump(int[] nums) {
        boolean[] dp = new boolean[nums.length];

        dp[nums.length - 1] = true;

        for (int i = nums.length - 2; i >= 0; --i) {
            for (int j = 0; j <= nums[i]; ++j) {
                if (i + j >= nums.length) {
                    break;
                }
                if (dp[i + j] == true) {
                    dp[i] = true;
                    break;
                }
            }
        }

        System.out.println(Arrays.toString(dp));

        return dp[0];
    }
}


public class JumpGame {
    public static void main(String[] args) {
        testSol(List.of(new int[] {0}), true);
        testSol(List.of(new int[] {2, 3, 1, 1, 4}), true);
        testSol(List.of(new int[] {3, 2, 1, 0, 4}), false);
        testSol(List.of(new int[] {2, 0, 0}), true);
    }

    static void testSol(List input, Object output) {
        // todo : input, output match
        int[] arg1 = (int[]) input.get(0);
        boolean out = (boolean) output;
        Solution sol = new Solution();
        // todo : solution match
        boolean res = sol.canJump(arg1);
        if (res == out) {
            System.out.println("O : " + res);
        } else {
            System.out.println("x : " + res + "	expect : " + out);
        }
    }
}
