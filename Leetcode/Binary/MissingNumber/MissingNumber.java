package Binary.MissingNumber;
// 268. Missing Number
// https://leetcode.com/problems/missing-number/

import java.util.Arrays;

// O(n)
class Solution {
    public int missingNumber(int[] nums) {
        int total = nums.length * (nums.length + 1) / 2;

        for (int i = 0; i < nums.length; ++i) {
            total -= nums[i];
        }

        return total;
    }
}


// O(n)
class Solution1 {
    public int missingNumber(int[] nums) {
        int result = nums.length;

        for (int i = 0; i < nums.length; ++i) {
            result = result ^ i ^ nums[i];
        }

        return result;
    }
}


// O(nlogn)
class Solution2 {
    public int missingNumber(int[] nums) {
        Arrays.sort(nums);

        for (int i = 0; i < nums.length; ++i) {
            if (i != nums[i]) {
                return i;
            }
        }
        return nums.length;
    }
}


public class MissingNumber {
    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.missingNumber(new int[] {3, 0, 1}));
        System.out.println(sol.missingNumber(new int[] {0, 1}));
        System.out.println(sol.missingNumber(new int[] {9, 6, 4, 2, 3, 5, 7, 0, 1}));
    }
}
