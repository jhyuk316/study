# 198. House Robber
# https://leetcode.com/problems/house-robber/

from typing import List


# O(n) 공간을 안써도 되지 않나?
# res[i] = max(res[i-1], (nums[i] + res[i]))
class Solution:
    def rob(self, nums: List[int]) -> int:
        before = 0
        now = 0  # before의 before

        for i in range(len(nums)):
            before, now = now, before
            now = max(before, (nums[i] + now))

        return now


# res[i] = max(res[i-1], (nums[i] + res[i-2]))
class Solution3:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        maxAmount = [0] * 3

        for i in range(len(nums)):
            maxAmount[2] = max(maxAmount[1], (nums[i] + maxAmount[0]))
            maxAmount[0] = maxAmount[1]
            maxAmount[1] = maxAmount[2]

        return maxAmount[2]


# O(n) i가 들어가는게 좋은지 안들어가는게 좋은지 판단
# res[i] = max(res[i-1], (nums[i] + res[i-2]))
class Solution2:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        maxAmount = [0] * len(nums)
        maxAmount[0] = nums[0]

        for i in range(1, len(nums)):
            maxAmount[i] = max(maxAmount[i - 1], (nums[i] + maxAmount[i - 2]))

        print(maxAmount)

        return maxAmount[-1]


# O(n) 1칸 건너 뛸 것인지 2칸 건너 뛸것인지 비교
# res[i] = nums[i] + max(res[i-2], res[i-3])
class Solution1:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        maxAmount = [0] * len(nums)
        maxAmount[0] = nums[0]
        maxAmount[1] = nums[1]

        for i in range(2, len(nums)):
            before1 = maxAmount[i - 2]
            before2 = maxAmount[i - 3]
            # i가 2일 때, -1이 되지만 최악의 경우(len:3일 때) 자기 자신이므로 0

            maxAmount[i] = nums[i] + max(before1, before2)

        print(maxAmount)

        return max(maxAmount[-1], maxAmount[-2])


if __name__ == "__main__":
    sol = Solution()

    print(sol.rob([9]))
    print(sol.rob([1, 2]))
    print(sol.rob([1, 2, 3, 1]))
    print(sol.rob([2, 7, 9, 3, 1]))
    print(sol.rob([2, 1, 1, 9, 7, 3, 1]))
