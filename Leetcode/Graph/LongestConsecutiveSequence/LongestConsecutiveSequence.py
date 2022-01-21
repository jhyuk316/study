# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List


# O(n) 해답 미쳤네. set을 만들고 머리를 찾고 길이 계산.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        maxLength = 0
        for num in nums:
            if num - 1 not in nums:
                tempLength = 1
                while num + tempLength in nums:
                    tempLength += 1
                maxLength = max(maxLength, tempLength)

        return maxLength


def testSol(func, input, output):
    res = func(input)
    if res == output:
        print(f"O : {res}")
    else:
        print(f"X : {res}	excpet : {output}")


if __name__ == "__main__":
    sol = Solution()

    testSol(sol.longestConsecutive, [100, 4, 200, 1, 3, 2], 4)
    testSol(sol.longestConsecutive, [0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9)
