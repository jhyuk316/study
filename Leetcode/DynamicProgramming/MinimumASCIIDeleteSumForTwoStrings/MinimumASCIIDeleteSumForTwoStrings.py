# 712. Minimum ASCII Delete Sum for Two Strings
# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

# O(n^2) dp[i][j] = max(d[i][j-1] + ord(c), d[i-1][j-1])
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [[0] * (len(s2) + 1) for _ in range(len(s1))]

        asciiS1 = 0
        asciiS2 = 0

        for c in s1:
            asciiS1 += ord(c)
        for c in s2:
            asciiS2 += ord(c)

        maxAscii = 0
        for i, c1 in enumerate(s1):
            for j, c2 in enumerate(s2):
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
                if c1 == c2:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + ord(c1))
                maxAscii = max(maxAscii, dp[i][j])

        print(asciiS1, asciiS2, maxAscii)
        print(*dp, sep="\n")

        return asciiS1 + asciiS2 - maxAscii * 2


def testSol(func, input, output):
    res = func(*input)
    if res == output:
        print(f"O : {res}")
    else:
        print(f"X : {res}	excpet : {output}")


if __name__ == "__main__":
    sol = Solution()

    testSol(sol.minimumDeleteSum, ("sea", "eat"), 231)
    testSol(sol.minimumDeleteSum, ("delete", "leet"), 403)
    testSol(sol.minimumDeleteSum, ("zzzzzaaaaaa", "azazazazaza"), 970)
