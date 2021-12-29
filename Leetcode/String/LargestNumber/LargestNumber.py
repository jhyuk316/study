# 179. Largest Number
# https://leetcode.com/problems/largest-number/

from typing import List
import functools

# O(n)
class Solution:
    def comp(self, a: str, b: str):
        # return -1 if int(a + b) > int(b + a) else 1
        return int(b + a) - int(a + b)

    def largestNumber(self, nums: List[int]) -> str:
        strNums = list(map(str, nums))

        strNums.sort(key=functools.cmp_to_key(self.comp))

        return str(int("".join(strNums)))
        # return "".join(strNums).lstrip("0") or "0"


if __name__ == "__main__":
    sol = Solution()

    print(sol.largestNumber([6, 10, 2, 5]))
    print(sol.largestNumber([6, 66, 2, 5]))
    print(sol.largestNumber([10, 2]))
    print(sol.largestNumber([0, 0, 0]))
