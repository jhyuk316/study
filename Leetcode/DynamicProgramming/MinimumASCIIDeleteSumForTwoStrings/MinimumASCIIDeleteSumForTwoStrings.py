# 712. Minimum ASCII Delete Sum for Two Strings
# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/


# O(n^2)
# dp[i][j] = max(dp[i][j-1], dp[i-1][j]) if c1 != c2
# dp[i][j] = d[i][j-1] + ord(c) if c1 = c2
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        s1 = list(map(ord, s1))
        s2 = list(map(ord, s2))

        asciiS1 = 0
        asciiS2 = 0
        for c in s1:
            asciiS1 += c
        for c in s2:
            asciiS2 += c

        dp = [[0] * (len(s2) + 1) for _ in range(len(s1))]
        for i, c1 in enumerate(s1):
            for j, c2 in enumerate(s2):
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
                if c1 == c2:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + c1)

        print(*dp, sep="\n")

        return asciiS1 + asciiS2 - dp[-1][-2] * 2


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
