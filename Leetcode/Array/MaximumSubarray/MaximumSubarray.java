package Array.MaximumSubarray;
// 53. Maximum Subarray
// https://leetcode.com/problems/maximum-subarray/

public class MaximumSubarray {
    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.maxSubArray(new int[] {-2, 1, -3, 4, -1, 2, 1, -5, 4}));
        System.out.println(sol.maxSubArray(new int[] {-2, 1, -3, 1, -1, 2, 1, -5, 2}));
        System.out.println(sol.maxSubArray(new int[] {1}));
        System.out.println(sol.maxSubArray(new int[] {1, -2}));
        System.out.println(sol.maxSubArray(new int[] {5, 4, -1, 7, 8}));
        System.out.println(sol.maxSubArray(new int[] {-10, -2, -3, -4}));

    }
}

// slide window - time limit exceeded
// class Solution {
// public int maxSubArray(int[] nums) {
// int max = nums[0];
// int wtemp;
// for (int w = 1; w <= nums.length; ++w) {
// wtemp = 0;
// for (int i = 0; i < w; ++i) {
// wtemp += nums[i];
// if (wtemp > max) {
// max = wtemp;
// }
// }
// for (int i = w; i < nums.length; ++i) {
// wtemp += nums[i];
// wtemp -= nums[i - w];

// if (wtemp > max) {
// max = wtemp;
// System.out.println(w + ": [" + (i - w + 1) + ", " + i + "] = " + max);
// }
// }
// }

// return max;
// }
// }


// O(n)
class Solution {
    public int maxSubArray(int[] nums) {
        int max = nums[0];
        int temp = 0;

        for (int i = 0; i < nums.length; ++i) {
            temp += nums[i];
            if (temp < nums[i]) {
                temp = nums[i];
            }
            if (temp > max) {
                max = temp;
            }
        }

        return max;
    }
}

// Divide and conquer Fail
// class Solution {
// public int maxSubArray(int[] nums) {
// return _maxSubArray(nums, 0, nums.length - 1, nums[0], nums[0])[0];
// }

// public int[] _maxSubArray(int[] nums, int left, int right, int max, int subSum) {
// // max, subSum
// if (left == right){
// if (subSum+nums[left] < nums[left]){
// subSum = nums[left];
// }
// if (subSum > max){
// max = subSum;
// }
// return new int[]{max, subSum};
// }

// int mid = (left + right) / 2;

// int[] leftRes = _maxSubArray(nums, left, mid, max, subSum);
// int[] rightRes = _maxSubArray(nums, mid + 1, right, max, subSum);

// subSum = Math.max(subSum, subSum + maxLeft);

// maxLeft = Math.max(maxLeft, maxLeft + subSum);
// maxRight = Math.max(maxRight, maxRight + subSum);

// max = Math.max(max, Math.max(maxLeft, maxRight));

// System.out.println(left + " " + right + ":" + max);
// return new int[] {max, subSum};
// }
// }


