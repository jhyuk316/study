# 91. Decode Ways
# https://leetcode.com/problems/decode-ways/


# O(n)
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[-1] = 1

        for i in range(1, len(s)):
            if 0 < int(s[i]) <= 9:
                dp[i] += dp[i - 1]

            if 10 <= int(s[i - 1 : i + 1]) <= 26:
                dp[i] += dp[i - 2]

        # print(dp)
        return dp[-2]


def testSol(func, input, output):
    res = func(input)
    if res == output:
        print(f"O : {res}")
    else:
        print(f"X : {res}\texcpet : {output}")


if __name__ == "__main__":
    sol = Solution()

    testSol(sol.numDecodings, "2", 1)
    testSol(sol.numDecodings, "12", 2)
    testSol(sol.numDecodings, "226", 3)
    testSol(sol.numDecodings, "06", 0)
    testSol(sol.numDecodings, "11106", 2)
    testSol(sol.numDecodings, "111", 3)
