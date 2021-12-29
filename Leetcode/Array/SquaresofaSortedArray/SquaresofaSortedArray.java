package Array.SquaresofaSortedArray;
// 977. Squares of a Sorted Array
// https://leetcode.com/problems/squares-of-a-sorted-array/

import java.util.Arrays;

public class SquaresofaSortedArray {
    public static void main(String[] args) {
        Solution sol = new Solution();

        int[] nums = {-7, -3, 2, 3, 10};
        int[] res = sol.sortedSquares(nums);
        System.out.println(Arrays.toString(res));

        int[] nums1 = {-7, -3, -1, 1};
        res = sol.sortedSquares(nums1);
        System.out.println(Arrays.toString(res));

        int[] nums2 = {-4, -4, -3};
        res = sol.sortedSquares(nums2);
        System.out.println(Arrays.toString(res));
    }
}


class Solution {
    public int[] sortedSquares(int[] nums) {
        int[] res = new int[nums.length];
        int origin = 0;
        int pos = 0;

        // 가장 절대값이 작은 숫자 찾기 origin
        for (int i = 1; i < nums.length; ++i) {
            if (Math.abs(nums[i - 1]) >= Math.abs(nums[i])) {
                origin = i;
            } else {
                break;
            }
        }

        // origin으로 부터 가까운 숫자부터 추가
        int before = origin - 1;
        int after = origin + 1;
        res[pos++] = nums[origin] * nums[origin];
        while (before >= 0 && after < nums.length) {
            if (Math.abs(nums[before]) > Math.abs(nums[after])) {
                res[pos++] = nums[after] * nums[after];
                after++;
            } else {
                res[pos++] = nums[before] * nums[before];
                before--;
            }
        }

        // 나머지 처리
        while (before >= 0) {
            res[pos++] = nums[before] * nums[before];
            before--;
        }
        while (after < nums.length) {
            res[pos++] = nums[after] * nums[after];
            after++;
        }
        return res;
    }
}
