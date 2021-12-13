package Array.threeSum;
// 15. 3Sum
// https://leetcode.com/problems/3sum/

import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;


class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();

        if (nums.length < 3) {
            return res;
        }

        Arrays.sort(nums);

        int i, j, k;
        for (i = 0; i < nums.length - 2; ++i) {
            if (i > 0 && nums[i] == nums[i - 1])
                continue;

            j = i + 1;
            k = nums.length - 1;
            while (j < k) {
                if (j > i + 1 && nums[j] == nums[j - 1]) {
                    j++;
                    continue;
                }
                if (k < nums.length - 1 && nums[k] == nums[k + 1]) {
                    k--;
                    continue;
                }

                if (nums[j] + nums[k] + nums[i] == 0) {
                    List<Integer> temp = new ArrayList<>();
                    temp.add(nums[i]);
                    temp.add(nums[j]);
                    temp.add(nums[k]);
                    res.add(temp);
                    j++;
                    k--;
                } else if (nums[j] + nums[k] + nums[i] > 0) {
                    k--;
                } else if (nums[j] + nums[k] + nums[i] < 0) {
                    j++;
                }
            }
        }
        return res;
    }
}


// O(n^2)
// 2개의 숫자를 결정하고 마지막 숫자를 map으로 찾음.
class Solution2 {
    public List<List<Integer>> threeSum(int[] nums) {
        if (nums.length < 3) {
            return new ArrayList<List<Integer>>();
        }

        Map<Integer, Integer> numMap = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; ++i) {
            if (numMap.containsKey(nums[i])) {
                numMap.put(nums[i], numMap.get(nums[i]) + 1);
            } else {
                numMap.put(nums[i], 1);
            }
        }

        Arrays.sort(nums);

        Set<List<Integer>> resSet = new HashSet<List<Integer>>();

        int target = 0;
        for (int i = 0; i < nums.length - 2; ++i) {
            if (nums[i] > 0) {
                break;
            }
            if (numMap.get(nums[i]) == 1) {
                numMap.remove(nums[i]);
            } else {
                numMap.put(nums[i], numMap.get(nums[i]) - 1);
            }

            for (int j = nums.length - 1; j > i; --j) {
                if (nums[j] < 0) {
                    break;
                }
                target = 0 - nums[i] - nums[j];

                if ((target == nums[j] && numMap.get(nums[j]) > 1)
                        || (target != nums[j] && numMap.containsKey(target))) {
                    List<Integer> temp = new ArrayList<Integer>();
                    temp.add(nums[i]);
                    temp.add(nums[j]);
                    temp.add(target);

                    // Collections.sort(temp);
                    resSet.add(temp);
                }
            }
        }

        List<List<Integer>> result = new ArrayList<>(resSet);
        return result;
    }
}


// O(n^2)
// 2개의 숫자를 결정하고 마지막 숫자를 binarySearch로 찾음.
class Solution1 {
    public List<List<Integer>> threeSum(int[] nums) {
        if (nums.length < 3) {
            return new ArrayList<List<Integer>>();
        }

        List<Integer> numList = new ArrayList<>();
        for (int num : nums) {
            numList.add(num);
        }
        Collections.sort(numList);

        Set<List<Integer>> resSet = new HashSet<List<Integer>>();

        for (int i = 0; i < nums.length - 2; ++i) {
            if (numList.get(i) > 0) {
                break;
            }
            for (int j = nums.length - 1; j > i; --j) {
                if (numList.get(j) < 0) {
                    break;
                }
                int target = 0 - numList.get(i) - numList.get(j);
                int k = binarySearch(numList, target, i + 1, j - 1);
                if (k != -1) {
                    List<Integer> temp = new ArrayList<Integer>();
                    temp.add(numList.get(i));
                    temp.add(numList.get(k));
                    temp.add(numList.get(j));
                    resSet.add(temp);
                }
            }
        }

        List<List<Integer>> result = new ArrayList<>(resSet);

        return result;
    }

    public int binarySearch(List<Integer> nums, int target, int left, int right) {
        int mid = 0;
        int temp = 0;
        while (left <= right) {
            mid = (left + right) / 2;
            temp = nums.get(mid);
            if (temp == target) {
                return mid;
            }
            if (temp > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return -1;
    }
}


public class threeSum {
    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.threeSum(new int[] {-1, 0, 1, 2, -1, -4}));

        // [[-2, -1, 3], [-3, 0, 3], [-2, 0, 2]]
        System.out.println(sol.threeSum(new int[] {-3, -2, -1, 0, 2, 3}));

        System.out.println(sol.threeSum(new int[] {0, 0, 0, 0}));
        // System.out.println(sol.threeSum(new int[] {1, 1, -2}));
        // System.out.println(sol.threeSum(new int[] {0, 2, 3}));
        // System.out.println(sol.threeSum(new int[] {-3, -2, -1}));
        // System.out.println(sol.threeSum(new int[] {-1, 0, 1, 0}));
        // System.out.println(sol.threeSum(new int[] {3, -2, 1, 0}));

        // System.out.println(sol.threeSum(new int[] {-100, 0, 10, 2, -1, -4}));
        // System.out.println(sol.threeSum(new int[] {0, 2, 0, 2, 0, -4}));
        // System.out.println(sol.threeSum(new int[] {}));
        // System.out.println(sol.threeSum(new int[] {0}));
    }

}

