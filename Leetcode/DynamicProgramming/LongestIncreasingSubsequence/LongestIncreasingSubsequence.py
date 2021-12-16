# 300. Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/

from typing import List

# O(n^2)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lengthList = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            temp = 0
            for j in reversed(range(i)):
                if nums[i] > nums[j]:
                    temp = max(temp, lengthList[j])
            lengthList[i] = temp + 1
        # print(lengthList)
        return max(lengthList)


if __name__ == "__main__":
    sol = Solution()
    # print(sol.lengthOfLIS([3, 1, 4, 2]))
    # print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(sol.lengthOfLIS([10, 9, 4, 5, 3, 7, 101, 18]))
    print(sol.lengthOfLIS([5, 2, 3, 7, 1, 4, 6]))
