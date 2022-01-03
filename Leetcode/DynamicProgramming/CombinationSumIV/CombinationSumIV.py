# 377. Combination Sum IV
# https://leetcode.com/problems/combination-sum-iv/

from typing import List


class Solution:
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
