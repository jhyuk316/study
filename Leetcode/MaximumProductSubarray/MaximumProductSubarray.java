package MaximumProductSubarray;
// 152. Maximum Product Subarray
// https://leetcode.com/problems/maximum-product-subarray/

import java.util.Vector;

// O(n) 양수와 음수로 나누어 음수가 곱해질때 서로 교체
// 예외가 존재하고, 간단해 보이는데 까다로운 디버깅이 필요함.
class Solution {
    public int maxProduct(int[] nums) {
        int plus = 1;
        int minus = 0;
        int max = nums[0];

        if (nums.length == 1) {
            return nums[0];
        }

        for (int i = 0; i < nums.length; ++i) {
            plus = plus == 0 ? nums[i] : plus * nums[i];
            minus = minus * nums[i];

            if (nums[i] < 0) {
                int temp = plus;
                plus = minus;
                minus = temp;
            }

            max = Math.max(max, plus);
            // System.out.println(i + ": " + max);
        }

        return max;
    }
}


// O(n) 앞 뒤로 한번씩 곱해서 max 갱신
// 간단한 원리, for문을 두번 돌아도 가장 빠름.
class Solution2 {
    public int maxProduct(int[] nums) {
        int temp = 1;
        int max = nums[0];

        for (int i = 0; i < nums.length; ++i) {
            temp *= nums[i];
            max = Math.max(max, temp);
            if (nums[i] == 0) {
                temp = 1;
            }
        }

        temp = 1;
        for (int i = nums.length - 1; i >= 0; --i) {
            temp *= nums[i];
            max = Math.max(max, temp);
            if (nums[i] == 0) {
                temp = 1;
            }
        }

        return max;
    }
}


public class MaximumProductSubarray {
    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.maxProduct(new int[] {10, -2, 5, -3, 5, -2, 4}));

        System.out.println(sol.maxProduct(new int[] {2, 3, -2, 4}));
        // System.out.println(sol.maxProduct(new int[] {2, -3, 2, 4}));

        System.out.println(sol.maxProduct(new int[] {-2, 0, -1}));
        System.out.println(sol.maxProduct(new int[] {-2, 0, -3, -4}));
        System.out.println(sol.maxProduct(new int[] {-1, -3, -2, 0, -1}));
        // System.out.println(sol.maxProduct(new int[] {-2, 0, 1}));

        System.out.println(sol.maxProduct(new int[] {-2}));
        // System.out.println(sol.maxProduct(new int[] {-4, -2, -7}));

        // System.out.println(sol.maxProduct(new int[] {2, 3, -2, 4, 0, 158, -2, 3, 4}));
        System.out.println(sol.maxProduct(new int[] {2, 0, -2, 0, 0, 158, -2, 0, 4}));
        // System.out.println(sol.maxProduct(new int[] {0, 0, 0}));
        System.out.println(sol.maxProduct(new int[] {-1, -3, -7, 0}));
        // System.out.println(sol.maxProduct(new int[] {-2, 3, 2, 4}));
        // System.out.println(sol.maxProduct(new int[] {1, -2, 3, 2, 4}));

    }

}


// O(n) 0 분할 후 - 분할 하여 접근, 느림
// 잘못된 발상, 문제를 분할하면 쉬울 줄 알았으나, 더욱 많은 절차로 느리고 복잡함.
class Solution3 {
    public int maxProduct(int[] nums) {
        Vector<Integer> zeroPos = new Vector<>();

        zeroPos.add(-1);
        for (int i = 0; i < nums.length; ++i) {
            if (nums[i] == 0) {
                zeroPos.add(i);
            }
        }
        zeroPos.add(nums.length);

        // System.out.println("zeroPos " + zeroPos);

        Vector<Integer> results = new Vector<>();
        if (zeroPos.size() > 2)
            results.add(0);

        for (int i = 0; i < zeroPos.size() - 1; ++i) {
            if (zeroPos.get(i + 1) - zeroPos.get(i) == 1) {
                continue;
            }
            results.add(maxProduct(nums, zeroPos.get(i) + 1, zeroPos.get(i + 1)));
        }

        // System.out.println(results);

        int max = -10000;
        for (int i = 0; i < results.size(); ++i) {
            if (results.get(i) > max) {
                max = results.get(i);
            }
        }

        return max;
    }

    public int maxProduct(int[] nums, int start, int end) {
        // System.out.println("s " + start + " e " + end);
        int prefix = 1;
        int full = 1;
        int suffix = 1;

        boolean firstMinus = false;

        if (end - start == 1) {
            return nums[start];
        }

        for (int i = start; i < end; ++i) {
            full *= nums[i];

            if (!firstMinus) {
                prefix *= nums[i];
            }

            if (nums[i] < 0) {
                firstMinus = true;
                suffix = 1;
            }

            suffix *= nums[i];
        }

        // System.out.println("pre " + prefix + " mid " + full + " suf " + suffix);

        if (full < 0) {
            full = Math.max(full / prefix, full / suffix);
        }

        return full;
    }
}
