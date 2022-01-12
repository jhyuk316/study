# 213. House Robber II
# https://leetcode.com/problems/house-robber-ii/

from typing import List

# O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)

        return max(self._rob(nums[:-1]), self._rob(nums[1:]))

    def _rob(self, nums: List[int]) -> int:
        before = 0
        now = 0  # before의 before

        for i in range(len(nums)):
            before, now = now, before
            now = max(before, (nums[i] + now))

        return now


# O(n)
class Solution1:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)

        money1 = [0] * len(nums)
        money2 = [0] * len(nums)

        money1[0] = nums[0]
        money1[1] = nums[1]

        money2[1] = nums[1]

        for i in range(1, len(nums) - 1):
            money1[i] = max(money1[i - 2] + nums[i], money1[i - 1])
            money2[i] = max(money2[i - 2] + nums[i], money2[i - 1])

        money2[-1] = max(money2[-3] + nums[-1], money2[-2])

        # print(money1)
        # print(money2)

        return max(money1[-2], money2[-1])


if __name__ == "__main__":
    sol = Solution()

    print(sol.rob([2]))
    print(sol.rob([3, 2]))
    print(sol.rob([2, 3, 2]))
    print(sol.rob([1, 2, 3, 1]))
    print(sol.rob([2, 2, 3, 1]))
    print(sol.rob([1, 7, 2, 3, 1]))
    print(sol.rob([1, 2, 3, 1, 5]))
    print(sol.rob([1, 2, 3, 1, 5, 6]))
    print(sol.rob([1, 2, 3, 1, 5, 6, 7]))
    print(sol.rob([1, 2, 3, 1, 6, 5, 7]))
    print(sol.rob([10, 1, 1, 10, 15]))
    print(sol.rob([10, 1, 10, 1, 15]))
    print(sol.rob([1, 10, 15, 10, 1]))
    print(sol.rob([15, 10, 1, 1, 10]))
    print(sol.rob([1, 15, 10, 1, 10]))
