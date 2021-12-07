# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n != 0:
            if (n & 1) == 1:
                count += 1
            n = n >> 1

        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.hammingWeight(11))
