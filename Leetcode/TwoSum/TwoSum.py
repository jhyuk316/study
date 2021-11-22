#  1. Two Sum
#  https://leetcode.com/problems/two-sum/

from typing import List

# O(n^2)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

# O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for idx, num in enumerate(nums):
            if (target - num) in dic:
                return [dic[target - num], idx]
            else:
                dic[num] = idx


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 13], 9))
    print(sol.twoSum([3, 2, 4], 6))
    print(sol.twoSum([9, 2, 3, 7, 8, 10, 4], 6))
