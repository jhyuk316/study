# 377. Combination Sum IV
# https://leetcode.com/problems/combination-sum-iv/

from typing import List

# O(n), dp[n] = sum(dp[n - num] for num in nums if n - nums >= 0)
# dp[0] = 1
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # 특정 숫자를 만드는 조합 수 저장
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(target + 1):
            sumDp = sum(dp[i - num] for num in nums if i - num >= 0)
            dp[i] += sumDp

        print(dp)
        return dp[target]


# O(n) dp[n] = sum(dp[n - num] for num in nums if n - nums >= 0)
class Solution1:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # 특정 숫자를 만드는 조합 수 저장
        dp = [0] * (target + 1)

        for num in nums:
            if target + 1 > num:
                dp[num] = 1

        for i in range(1, target + 1):
            sum = 0
            for num in nums:
                if i - num < 0:
                    continue

                sum += dp[i - num]

            dp[i] += sum

        print(dp)
        return dp[target]


if __name__ == "__main__":
    sol = Solution()

    print(sol.combinationSum4([1, 2, 3], 4))
    print(sol.combinationSum4([1, 2, 3], 5))
    print(sol.combinationSum4([9], 3))
