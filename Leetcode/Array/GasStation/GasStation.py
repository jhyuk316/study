# 134. Gas Station
# https://leetcode.com/problems/gas-station/


from typing import List

# O(n)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        sumBenfit = 0
        minSum = 2 ^ 31 - 1
        minSumPos = -1

        for i in range(len(gas)):
            benefit = gas[i] - cost[i]
            sumBenfit += benefit
            if minSum > sumBenfit:
                minSum = sumBenfit
                minSumPos = i

        return (minSumPos + 1) % len(gas)


if __name__ == "__main__":
    sol = Solution()

    print(sol.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
    print(sol.canCompleteCircuit([10, 2, 3, 4, 1], [3, 4, 5, 5, 2]))
    print(sol.canCompleteCircuit([2, 3, 4], [3, 4, 3]))
