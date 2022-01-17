# 62. Unique Paths
# https://leetcode.com/problems/unique-paths/


# O(n) combination 계산 (m+n-2)Cn if n < m
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num = m + n - 1
        combi = min(m, n) - 1

        result = 1
        for i in range(1, combi + 1):
            result *= num - i
            result /= i

        return int(result)


# O(m*n) dp[i] += dp[i - 1]
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n

        for _ in range(1, m):
            for i in range(1, n):
                dp[i] += dp[i - 1]

        return dp[-1]


# O(m*n) dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


def testSol(func, input, output):
    res = func(*input)
    if res == output:
        print(f"O : {res}")
    else:
        print(f"X : {res}	excpet : {output}")


if __name__ == "__main__":
    sol = Solution()

    testSol(sol.uniquePaths, (3, 7), 28)
    testSol(sol.uniquePaths, (3, 2), 3)
    testSol(sol.uniquePaths, (8, 20), 657800)
    testSol(sol.uniquePaths, (15, 19), 471435600)
    testSol(sol.uniquePaths, (30, 20), 11541847896480)
    testSol(sol.uniquePaths, (50, 50), 25477612258980856902730428600)
    testSol(
        sol.uniquePaths,
        (100, 100),
        22750883079422934966181954039568885395604168260154104734000,
    )
