# 417. Pacific Atlantic Water Flow
# https://leetcode.com/problems/pacific-atlantic-water-flow/

"""
큰 문제는 쪼개자! 한 번에 해결하려고 하면 안 된다.
"""

from enum import Enum
from typing import Dict, List


def printMap(islandMap):
    for i, row in enumerate(islandMap):
        for j, h in enumerate(row):
            print("■" if h else "□", end=" ")
            if j % 5 == 4:
                print(" ", end=" ")

        print()
        if i % 5 == 4:
            print()


# O(m*n) memorization
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M = len(heights)
        N = len(heights[0])

        isPacificMap = [[False] * N for _ in range(M)]
        isAtlanticMap = [[False] * N for _ in range(M)]

        def dfs(x, y, mapName):
            if mapName[x][y]:
                return

            mapName[x][y] = True

            height = heights[x][y]
            if x - 1 >= 0 and heights[x - 1][y] >= height:
                dfs(x - 1, y, mapName)
            if x + 1 < M and heights[x + 1][y] >= height:
                dfs(x + 1, y, mapName)
            if y - 1 >= 0 and heights[x][y - 1] >= height:
                dfs(x, y - 1, mapName)
            if y + 1 < N and heights[x][y + 1] >= height:
                dfs(x, y + 1, mapName)

        for i in range(M):
            dfs(i, 0, isPacificMap)
            dfs(i, N - 1, isAtlanticMap)
        for j in range(N):
            dfs(0, j, isPacificMap)
            dfs(M - 1, j, isAtlanticMap)

        # printMap(isPacificMap)
        # printMap(isAtlanticMap)

        res = []
        for i in range(M):
            for j in range(N):
                if isPacificMap[i][j] and isAtlanticMap[i][j]:
                    res.append([i, j])
        return res


# O(m*n???) FAIL 두 개를 동시에 하는 것은 말이 안 되는 것이었음.
class SolutionFAIL:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        class Visit(Enum):
            before = 0
            doing = 1
            finish = 2

        M = len(heights)
        N = len(heights[0])

        isPacificMap = [[False] * N for _ in range(M)]
        isAtlanticMap = [[False] * N for _ in range(M)]
        visitedMap = [[Visit.before] * N for _ in range(M)]

        def dfs(x, y, isPacific, isAtlantic):
            if visitedMap[x][y] != Visit.before:
                return

            visitedMap[x][y] = Visit.doing
            isPacificMap[x][y] = isPacificMap[x][y] or isPacific
            isAtlanticMap[x][y] = isAtlanticMap[x][y] or isAtlantic

            height = heights[x][y]
            if x - 1 >= 0 and heights[x - 1][y] >= height:
                dfs(x - 1, y, isPacificMap[x][y], isAtlanticMap[x][y])
            if x + 1 < M and heights[x + 1][y] >= height:
                dfs(x + 1, y, isPacificMap[x][y], isAtlanticMap[x][y])
            if y - 1 >= 0 and heights[x][y - 1] >= height:
                dfs(x, y - 1, isPacificMap[x][y], isAtlanticMap[x][y])
            if y + 1 < N and heights[x][y + 1] >= height:
                dfs(x, y + 1, isPacificMap[x][y], isAtlanticMap[x][y])

            visitedMap[x][y] = Visit.before

            if isPacificMap[x][y] and isAtlanticMap[x][y]:
                visitedMap[x][y] = Visit.finish

        for i in range(M):
            dfs(i, 0, True, False)
            dfs(i, N - 1, False, True)

        for j in range(N):
            dfs(0, j, True, False)
            dfs(M - 1, j, False, True)

        # for i in range(M):
        #     for j in range(N):
        #         dfs(i, j, False, False)

        # printMap(isPacificMap)
        # printMap(isAtlanticMap)

        res = []
        for i, rows in enumerate(heights):
            for j, height in enumerate(rows):
                if isPacificMap[i][j] and isAtlanticMap[i][j]:
                    res.append([i, j])
        return res


# O(m*n) FAIL bottom-up은 안 되는 것인가?
class SolutionFAIL:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        class Visit(Enum):
            before = 0
            doing = 1
            finish = 2

        M = len(heights)
        N = len(heights[0])

        isPacificMap: List[List[bool]] = [[False] * N for _ in range(M)]
        isAtlanticMap: List[List[bool]] = [[False] * N for _ in range(M)]
        visitedMap: List[List[Visit]] = [[Visit.before] * N for _ in range(M)]
        # 0 :

        def pacificDFS(x, y) -> bool:
            if x == 3 and y == 27:
                print(x, y)
            if x - 1 < 0 or y - 1 < 0:
                visitedMap[x][y] = Visit.finish
                isPacificMap[x][y] = True
                return True

            if visitedMap[x][y] == Visit.finish:
                return isPacificMap[x][y]

            if visitedMap[x][y] == Visit.doing:
                return

            visitedMap[x][y] = Visit.doing
            isPacific = False
            # 상하 좌우
            if x - 1 >= 0 and heights[x - 1][y] < heights[x][y]:
                isPacific = isPacific or pacificDFS(x - 1, y)
            if x + 1 < M and heights[x + 1][y] < heights[x][y]:
                isPacific = isPacific or pacificDFS(x + 1, y)
            if y - 1 >= 0 and heights[x][y - 1] < heights[x][y]:
                isPacific = isPacific or pacificDFS(x, y - 1)
            if y + 1 < N and heights[x][y + 1] < heights[x][y]:
                isPacific = isPacific or pacificDFS(x, y + 1)

            visitedMap[x][y] = Visit.finish
            isPacificMap[x][y] = isPacific
            return isPacific

        def atlanticDFS(x, y) -> None:
            if x + 1 >= M or y + 1 >= N:
                visitedMap[x][y] = True
                isAtlanticMap[x][y] = True
                return True

            if visitedMap[x][y]:
                return isAtlanticMap[x][y]

            visitedMap[x][y] = True
            isAtlantic = False
            # 상하 좌우
            if x - 1 >= 0 and heights[x - 1][y] <= heights[x][y]:
                isAtlantic = isAtlantic or atlanticDFS(x - 1, y)
            if x + 1 < M and heights[x + 1][y] <= heights[x][y]:
                isAtlantic = isAtlantic or atlanticDFS(x + 1, y)
            if y - 1 >= 0 and heights[x][y - 1] <= heights[x][y]:
                isAtlantic = isAtlantic or atlanticDFS(x, y - 1)
            if y + 1 < N and heights[x][y + 1] <= heights[x][y]:
                isAtlantic = isAtlantic or atlanticDFS(x, y + 1)

            isAtlanticMap[x][y] = isAtlantic
            return isAtlantic

        for i, rows in enumerate(heights):
            for j, height in enumerate(rows):
                pacificDFS(i, j)

        visitedMap: List[List[bool]] = [[False] * N for _ in range(M)]
        for i, rows in enumerate(heights):
            for j, height in enumerate(rows):
                atlanticDFS(i, j)

        printMap(isPacificMap)
        print()
        printMap(isAtlanticMap)

        res = []
        for i, rows in enumerate(heights):
            for j, height in enumerate(rows):
                if isPacificMap[i][j] and isAtlanticMap[i][j]:
                    res.append([i, j])

        return res


def testSol(func, input, output):
    res = func(input)
    if res == output:
        print(f"O : {res}")
    else:
        print(f"X : {res}	excpet : {output}")


if __name__ == "__main__":
    sol = Solution()

    testSol(
        sol.pacificAtlantic,
        [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ],
        [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
    )
    testSol(sol.pacificAtlantic, [[2, 1], [1, 2]], [[0, 0], [0, 1], [1, 0], [1, 1]])
    testSol(
        sol.pacificAtlantic,
        [[5, 5, 5], [5, 1, 5], [5, 5, 5]],
        [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]],
    )
    testSol(
        sol.pacificAtlantic,
        [[4, 4, 4, 5], [1, 1, 1, 2], [1, 2, 1, 2], [1, 2, 2, 2], [3, 1, 1, 1]],
        [[0, 3], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2], [3, 3], [4, 0]],
    )
