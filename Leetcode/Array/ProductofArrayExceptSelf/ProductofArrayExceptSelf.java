package Array.ProductofArrayExceptSelf;
// 238. Product of Array Except Self
// https://leetcode.com/problems/product-of-array-except-self/

import java.util.Arrays;

public class ProductofArrayExceptSelf {
    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(Arrays.toString(sol.productExceptSelf(new int[] {1, 2, 3, 4})));
        System.out.println(Arrays.toString(sol.productExceptSelf(new int[] {-1, 1, 0, -3, 3})));

    }
}

// time O(n)
// class Solution {
// public int[] productExceptSelf(int[] nums) {
// int[] result = new int[nums.length];
// int[] prefix = new int[nums.length];
// int[] suffix = new int[nums.length];

// // |0...k-1|k|k+1...n|
// int temp = 1;
// for(int i = 0 ; i < nums.length-1; ++i){
// temp = temp * nums[i];
// prefix[i] = temp;
// }

// temp = 1;
// for(int i = nums.length-1 ; i > 0 ; --i){
// temp = temp * nums[i];
// suffix[i] = temp;
// }

// for (int i = 1; i < nums.length - 1; ++i) {
// result[i] = prefix[i-1] * suffix[i+1];
// }
// result[0] = suffix[1];
// result[nums.length - 1] = prefix[nums.length - 2];

// // System.out.println("pre " + Arrays.toString(prefix));
// // System.out.println("suf " + Arrays.toString(suffix));

// return result;
// }
// }


// O(n) without extra space
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] result = new int[nums.length];

        // |0...k-1|k|k+1...n|
        int temp = 1;
        for (int i = 0; i < nums.length; ++i) {
            result[i] = temp;
            temp *= nums[i];
        }
        // System.out.println("res " + Arrays.toString(result));

        temp = 1;
        for (int i = nums.length - 1; i >= 0; --i) {
            result[i] *= temp;
            temp *= nums[i];
        }
        // System.out.println("res " + Arrays.toString(result));

        return result;
    }
}
