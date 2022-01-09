# 179. Largest Number
# https://leetcode.com/problems/largest-number/

from typing import List
import functools


# O(nlongn) : 정수 비교
class Solution:
    def comp(self, a: int, b: int):
        countA = len(str(a))
        countB = len(str(b))

        return (b * 10 ** countA + a) - (a * 10 ** countB + b)

    def largestNumber(self, nums: List[int]) -> str:
        nums.sort(key=functools.cmp_to_key(self.comp))
        print(nums)

        return str(int("".join(map(str, nums))))


# O(nlogn) : 문자 비교
class Solution1:
    def comp(self, a: str, b: str):
        return -1 if a + b > b + a else 1
        # return int(b + a) - int(a + b)

    def largestNumber(self, nums: List[int]) -> str:
        strNums = list(map(str, nums))

        strNums.sort(key=functools.cmp_to_key(self.comp))

        return str(int("".join(strNums)))
        # return "".join(strNums).lstrip("0") or "0"


if __name__ == "__main__":
    sol = Solution()

    print(sol.largestNumber([62, 626]))
    print(sol.largestNumber([6, 10, 2, 5]))
    print(sol.largestNumber([6, 2, 5, 66]))
    print(sol.largestNumber([0, 10, 2]))
    print(sol.largestNumber([0, 0, 0]))
    print(sol.largestNumber([0, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
