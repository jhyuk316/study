# 73. Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/
#
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -2^31 <= matrix[i][j] <= 2^31

from typing import List

# space : O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # 0번 row, 0번 col check
        isZeroRow0 = True if 0 in matrix[0] else False
        isZeroCol0 = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                isZeroCol0 = True
                break

        # set flag
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if i == 0 or j == 0:
                    continue
                if col == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # print("\nflag", *matrix, sep="\n")

        # change
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        # print("\nchange", *matrix, sep="\n")

        # change Row0, Col0
        if isZeroRow0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        if isZeroCol0:
            for i in range(len(matrix)):
                matrix[i][0] = 0


# space : O(n)
class Solution2:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        colList = set()

        for i, row in enumerate(matrix):
            hasZeroRow = False
            for j, col in enumerate(row):
                if col == 0:
                    colList.add(j)
                    hasZeroRow = True
            if hasZeroRow:
                for j, col in enumerate(row):
                    row[j] = 0

        for i, row in enumerate(matrix):
            for j in colList:
                matrix[i][j] = 0


# space : O(mn)
class Solution1:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        posList = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    posList.append([i, j])

        for pos in posList:
            self._setZeroes(matrix, pos[0], pos[1])

    def _setZeroes(self, matrix: List[List[int]], row: int, col: int) -> None:
        for i in range(len(matrix)):
            matrix[i][col] = 0
        for j in range(len(matrix[0])):
            matrix[row][j] = 0


if __name__ == "__main__":
    sol = Solution()

    m1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print("-" * 10, *m1, sep="\n")
    sol.setZeroes(m1)
    print("result", *m1, sep="\n")

    m2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    print("-" * 10, *m2, sep="\n")
    sol.setZeroes(m2)
    print("result", *m2, sep="\n")

    m3 = [[1, 0, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    print("-" * 10, *m3, sep="\n")
    sol.setZeroes(m3)
    print("result", *m3, sep="\n")

    m4 = [[1, 1, 2, 1], [1, 0, 5, 2], [1, 3, 1, 5]]
    print("-" * 10, *m4, sep="\n")
    sol.setZeroes(m4)
    print("result", *m4, sep="\n")
