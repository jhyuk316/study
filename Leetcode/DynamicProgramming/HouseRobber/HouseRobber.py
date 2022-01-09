# 198. House Robber
# https://leetcode.com/problems/house-robber/

from typing import List


# O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        maxAmoutnt = [0] * len(nums)
        maxAmoutnt[0] = nums[0]
        maxAmoutnt[1] = nums[1]

        for i in range(2, len(nums)):
            before1 = maxAmoutnt[i - 2]
            before2 = maxAmoutnt[i - 3]
            # i가 2일 때, -1이 되지만 최악의 경우(len:3일 때) 자기 자신이므로 0

            maxAmoutnt[i] = nums[i] + max(before1, before2)

        # print(maxAmoutnt)

        return max(maxAmoutnt[-1], maxAmoutnt[-2])


if __name__ == "__main__":
    sol = Solution()

    print(sol.rob([9]))
    print(sol.rob([1, 2]))
    print(sol.rob([1, 2, 3, 1]))
    print(sol.rob([2, 7, 9, 3, 1]))
    print(sol.rob([2, 1, 1, 9, 7, 3, 1]))
