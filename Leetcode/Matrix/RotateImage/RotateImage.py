# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/

from typing import List


# O(n^2)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)

        for i in range(N // 2):
            for j in range(i, N - i - 1):
                temp = matrix[N - j - 1][i]
                matrix[N - j - 1][i] = matrix[N - i - 1][N - j - 1]
                matrix[N - i - 1][N - j - 1] = matrix[j][N - i - 1]
                matrix[j][N - i - 1] = matrix[i][j]
                matrix[i][j] = temp
        return matrix


def testSol(func, input, output):
    res = func(input)
    if res == output:
        print(f"O : {res}")
    else:
        print(f"X : {res}	excpet : {output}")


if __name__ == "__main__":
    sol = Solution()
    testSol(
        sol.rotate, [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    )
    testSol(
        sol.rotate,
        [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
        [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
    )
