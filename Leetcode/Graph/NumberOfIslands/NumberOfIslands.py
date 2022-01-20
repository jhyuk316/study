# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/


from typing import List

# (m*n) DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M = len(grid)
        N = len(grid[0])

        def dfs(x, y, num):
            grid[x][y] = num

            if x - 1 >= 0 and grid[x - 1][y] == "1":
                dfs(x - 1, y, num)
            if x + 1 < M and grid[x + 1][y] == "1":
                dfs(x + 1, y, num)
            if y - 1 >= 0 and grid[x][y - 1] == "1":
                dfs(x, y - 1, num)
            if y + 1 < N and grid[x][y + 1] == "1":
                dfs(x, y + 1, num)

        num = 1
        for i, rows in enumerate(grid):
            for j, col in enumerate(rows):
                if col == "1":
                    dfs(i, j, num)
                    num += 1

        # print(*grid, sep="\n")
        return num - 1


def testSol(func, input, output):
    res = func(input)
    if res == output:
        print(f"O : {res}")
    else:
        print(f"X : {res}	excpet : {output}")


if __name__ == "__main__":
    sol = Solution()

    testSol(
        sol.numIslands,
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ],
        1,
    )
    testSol(
        sol.numIslands,
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ],
        3,
    )
    testSol(
        sol.numIslands,
        [
            ["0", "0", "1", "1", "1"],
            ["1", "1", "0", "0", "1"],
            ["1", "0", "1", "0", "1"],
            ["0", "0", "1", "1", "1"],
            ["1", "1", "0", "0", "0"],
        ],
        3,
    )
