# 69. Sqrt(x)
# https://leetcode.com/problems/sqrtx/


# O(logn) Binary-Search
class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        right = x
        left = 0

        # count = 0
        while left < right:
            mid = (right + left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid
            # count += 1

        # print(left - 1, count)
        return left - 1


# O(logn) Babylonian method
class Solution2:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        sqrt = x / 100
        # count = 0
        while abs(sqrt - 0.5 * (sqrt + x / sqrt)) > 0.00001:
            sqrt = 0.5 * (sqrt + x / sqrt)
            # count += 1

        # print(sqrt, count)
        return int(sqrt)


# O(n) Brute-Force
class Solution1:
    def mySqrt(self, x: int) -> int:
        sqrt = 1
        while sqrt * sqrt <= x:
            sqrt += 1

        return sqrt - 1


def testSol(func, input, output):
    res = func(input)
    if res == output:
        print(f"O : {res}")
    else:
        print(f"X : {res}	excpet : {output}")


if __name__ == "__main__":
    sol = Solution()

    testSol(sol.mySqrt, 0, 0)
    testSol(sol.mySqrt, 1, 1)
    testSol(sol.mySqrt, 2, 1)
    testSol(sol.mySqrt, 4, 2)
    testSol(sol.mySqrt, 8, 2)
    testSol(sol.mySqrt, 9, 3)
    testSol(sol.mySqrt, 325732, 570)
    testSol(sol.mySqrt, 2147395599, 46339)
    testSol(sol.mySqrt, 2147483647, 46340)
    testSol(sol.mySqrt, 1073741823, 32767)
