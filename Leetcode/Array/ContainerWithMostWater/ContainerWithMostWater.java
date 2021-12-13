package Array.ContainerWithMostWater;
// 11. Container With Most Water
// https://leetcode.com/problems/container-with-most-water/


// O(n)
class Solution {
    public int maxArea(int[] height) {
        int maxWater = 0;
        int left = 0;
        int right = height.length - 1;

        while (left < right) {
            maxWater = Math.max(maxWater, calculateWater(height, left, right));
            if (height[left] < height[right]) {
                left++;
            } else {
                --right;
            }
        }

        return maxWater;
    }

    public int calculateWater(int[] height, int left, int right) {
        int maxHeight = Math.min(height[left], height[right]);
        int width = right - left;
        return maxHeight * width;
    }
}


// O(n^2)
class Solution1 {
    public int maxArea(int[] height) {
        int maxWater = 0;
        for (int i = 0; i < height.length; ++i) {
            for (int j = height.length - 1; j > i; --j) {
                if (height[i] <= height[j]) {
                    maxWater = Math.max(maxWater, calculateWater(height, i, j));
                    // System.out.println(i + ", " + j);
                    break;
                }
            }

            for (int k = 0; k < i; ++k) {
                if (height[i] <= height[k]) {
                    maxWater = Math.max(maxWater, calculateWater(height, k, i));
                    // System.out.println(i + ", " + k);
                    break;
                }
            }
        }

        return maxWater;
    }

    public int calculateWater(int[] height, int left, int right) {
        int maxHeight = Math.min(height[left], height[right]);
        int width = right - left;
        return maxHeight * width;
    }
}


public class ContainerWithMostWater {
    public static void main(String[] args) {
        Solution sol = new Solution();

        System.out.println(sol.maxArea(new int[] {1, 1, 21, 6, 9, 100, 20, 4, 8, 3, 7, 1}));
        System.out.println(sol.maxArea(new int[] {1, 7, 3, 8, 4, 20, 100, 20, 4, 8, 3, 7, 1}));
        System.out.println(sol.maxArea(new int[] {1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1}));

        System.out.println(sol.maxArea(new int[] {1, 8, 6, 9, 8, 9, 4, 8, 3, 7}));
        System.out.println(sol.maxArea(new int[] {1, 6, 8, 9, 8, 4, 8, 1, 1}));
        System.out.println(sol.maxArea(new int[] {1, 8, 6, 2, 5, 4, 8, 3, 7}));

        System.out.println(sol.maxArea(new int[] {1, 8, 6, 2, 5, 4, 8, 3, 100}));
        System.out.println(sol.maxArea(new int[] {100, 8, 6, 2, 5, 4, 8, 3, 1}));
        System.out.println(sol.maxArea(new int[] {1, 99, 6, 2, 5, 4, 8, 100, 1}));
        System.out.println(sol.maxArea(new int[] {1, 9, 6, 2, 5, 4, 8, 100, 1, 99, 99}));

        System.out.println(sol.maxArea(new int[] {1, 1}));
        System.out.println(sol.maxArea(new int[] {4, 3, 2, 1, 4}));
        System.out.println(sol.maxArea(new int[] {1, 8, 10, 19, 1}));
    }
}
