package DynamicProgramming.ClimbingStairs;
// 70. Climbing Stairs
// https://leetcode.com/problems/climbing-stairs/

// O(n)
class Solution {
    static int[] climb = new int[46];

    public int climbStairs(int n) {

        if (climb[n] != 0) {
            return climb[n];
        }

        if (n == 1) {
            return 1;
        }
        if (n == 2) {
            return 2;
        }

        climb[n] = climbStairs(n - 1) + climbStairs(n - 2);

        return climb[n];
    }
}


// O(n)
class Solution1 {
    public int climbStairs(int n) {
        int[] steps = new int[46];

        steps[1] = 1;
        steps[2] = 2;

        for (int i = 3; i <= n; ++i) {
            steps[i] = steps[i - 1] + steps[i - 2];
        }

        return steps[n];
    }
}


public class ClimbingStairs {
    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.climbStairs(2));
        System.out.println(sol.climbStairs(3));
        System.out.println(sol.climbStairs(45));
    }

}
