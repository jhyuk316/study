# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/

from typing import List


# O(mn) : 너무 지저분한 코드
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        top = -1
        bottom = len(matrix)
        left = -1
        right = len(matrix[0])

        row = 0
        col = 0

        # while col != left and col != right and row != top and row != bottom:
        while True:
            if col >= right:
                break
            while col < right:
                result.append(matrix[row][col])
                col += 1
            col -= 1
            row += 1
            top += 1

            if row >= bottom:
                break
            while row < bottom:
                result.append(matrix[row][col])
                row += 1
            row -= 1
            col -= 1
            right -= 1

            if col <= left:
                break
            while col > left:
                result.append(matrix[row][col])
                col -= 1
            col += 1
            row -= 1
            bottom -= 1

            if row <= top:
                break
            while row > top:
                result.append(matrix[row][col])
                row -= 1
            row += 1
            col += 1
            left += 1

        return result


if __name__ == "__main__":
    sol = Solution()

    print(sol.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(sol.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
    print(
        sol.spiralOrder(
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ]
        )
    )
