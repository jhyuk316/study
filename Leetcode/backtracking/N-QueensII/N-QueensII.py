# 52. N-Queens II
# https://leetcode.com/problems/n-queens-ii/


from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        qList = [-1] * n
        self.count = 0

        self._totalNQueens(n, 0, qList)

        return self.count

    def _totalNQueens(self, n: int, line: int, qList: List[int]) -> None:
        if n == line:
            # print(qList)
            self.count += 1
            return

        # cheak
        for i in range(n):
            for j in range(line):
                if qList[j] == i:
                    break

                if i == qList[j] - (line - j) or i == qList[j] + (line - j):
                    break
            else:
                qList[line] = i
                self._totalNQueens(n, line + 1, qList)
                qList[line] = -1


if __name__ == "__main__":
    sol = Solution()

    print(sol.totalNQueens(4))
    print(sol.totalNQueens(8))
    print(sol.totalNQueens(9))
