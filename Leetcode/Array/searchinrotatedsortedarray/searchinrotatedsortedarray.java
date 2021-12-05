package Array.searchinrotatedsortedarray;
// 33. Search in Rotated Sorted Array
// https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution {
    public int search(int[] nums, int target) {
        int minPos = findMin(nums);

        if (minPos == 0) {
            return binarySearch(nums, target, minPos, nums.length - 1);
        }

        if (nums[minPos] <= target && nums[nums.length - 1] >= target) {
            return binarySearch(nums, target, minPos, nums.length - 1);
        } else if (nums[0] <= target && nums[minPos - 1] >= target) {
            return binarySearch(nums, target, 0, minPos - 1);
        }

        return -1;
    }

    public int findMin(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        int mid = (left + right) / 2;

        if (nums[left] < nums[right]) {
            return left;
        }

        while (left < right) {
            mid = (left + right) / 2;

            if (nums[left] > nums[mid]) {
                right = mid;
            } else if (nums[right] < nums[mid]) {
                left = mid + 1;
            } else {
                return left;
            }
        }

        return left;
    }

    public int binarySearch(int[] nums, int target, int left, int right) {
        while (left <= right) {
            int mid = (left + right) / 2;

            if (target == nums[mid]) {
                return mid;
            } else if (target > nums[mid]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return -1;
    }
}


public class searchinrotatedsortedarray {

    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.search(new int[] {4, 5, 6, 7, 0, 1, 2}, 0));
        System.out.println(sol.search(new int[] {4, 5, 6, 7, 0, 1, 2}, 5));
        System.out.println(sol.search(new int[] {4, 5, 6, 7, 0, 1, 2}, 3));
        System.out.println(sol.search(new int[] {4, 5, 6, 8, 0, 1, 2}, 7));
        System.out.println(sol.search(new int[] {0, 1, 2, 4, 5, 6, 8}, 7));
        System.out.println(sol.search(new int[] {1}, 0));
        System.out.println(sol.search(new int[] {1}, 1));
        System.out.println(sol.search(new int[] {1}, 2));
        System.out.println(sol.search(new int[] {5, 1, 2, 3, 4}, 1));


    }
}
