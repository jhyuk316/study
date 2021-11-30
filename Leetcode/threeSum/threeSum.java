package threeSum;
// 15. 3Sum
// https://leetcode.com/problems/3sum/

import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;


class Solution {
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

        // System.out.println(numMap);

        Set<List<Integer>> resSet = new HashSet<List<Integer>>();

        int target = 0;
        for (int i = 0; i < nums.length - 2; ++i) {
            if (numMap.get(nums[i]) == 1) {
                numMap.remove(nums[i]);
            } else {
                numMap.put(nums[i], numMap.get(nums[i]) - 1);
            }

            Map<Integer, Integer> tempMap = new HashMap<>(numMap);
            // System.out.println(tempMap);

            for (int j = i + 1; j < nums.length - 1; ++j) {
                if (tempMap.get(nums[j]) == 1) {
                    tempMap.remove(nums[j]);
                } else {
                    tempMap.put(nums[j], tempMap.get(nums[j]) - 1);
                }

                target = 0 - nums[i] - nums[j];

                if (tempMap.containsKey(target)) {
                    List<Integer> temp = new ArrayList<Integer>();
                    temp.add(nums[i]);
                    temp.add(nums[j]);
                    temp.add(target);

                    Collections.sort(temp);
                    resSet.add(temp);
                }
            }
        }

        List<List<Integer>> result = new ArrayList<>(resSet);
        return result;
    }
}


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
            for (int j = i + 1; j < nums.length - 1; ++j) {
                int target = 0 - numList.get(i) - numList.get(j);
                int k = binarySearch(numList, target, j + 1, numList.size() - 1);
                if (k != -1) {
                    List<Integer> temp = new ArrayList<Integer>();
                    temp.add(numList.get(i));
                    temp.add(numList.get(j));
                    temp.add(numList.get(k));
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
        // System.out.println(sol.threeSum(new int[] {-100, 0, 10, 2, -1, -4}));
        // System.out.println(sol.threeSum(new int[] {0, 0, 0, 2, 0, -4}));
        // System.out.println(sol.threeSum(new int[] {}));
        // System.out.println(sol.threeSum(new int[] {0}));
    }

}

