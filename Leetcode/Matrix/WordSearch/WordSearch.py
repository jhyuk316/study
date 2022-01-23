# 79. Word Search
# https://leetcode.com/problems/word-search/


from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.M = len(board)
        self.N = len(board[0])

        self.board = board
        self.word = word
        self.visited = [[False] * len(board[0]) for _ in range(len(board))]

        start = word[0]
        for i, rows in enumerate(board):
            for j, c in enumerate(rows):
                if c == start:
                    if self.findCharacter(i, j, 0):
                        return True

        return False

    def findCharacter(self, i, j, cPos):
        if self.visited[i][j] == True:
            return False

        if self.word[cPos] != self.board[i][j]:
            return False

        # 이미 문자는 같음. 끝이면 True
        if cPos == len(self.word) - 1:
            return True

        self.visited[i][j] = True

        res = False
        if i - 1 >= 0:
            res = res or self.findCharacter(i - 1, j, cPos + 1)
        if i + 1 < self.M:
            res = res or self.findCharacter(i + 1, j, cPos + 1)
        if j - 1 >= 0:
            res = res or self.findCharacter(i, j - 1, cPos + 1)
        if j + 1 < self.N:
            res = res or self.findCharacter(i, j + 1, cPos + 1)

        self.visited[i][j] = False

        return res


def testSol(func, input, output):
    res = func(*input)
    if res == output:
        print(f"O : {res}")
    else:
        print(f"X : {res}	excpet : {output}")


if __name__ == "__main__":
    sol = Solution()

    testSol(
        sol.exist,
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"),
        True,
    )
    testSol(
        sol.exist,
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ADFSA"),
        True,
    )
    testSol(
        sol.exist,
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"),
        True,
    )
    testSol(
        sol.exist,
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"),
        False,
    )
    testSol(
        sol.exist,
        ([["A"]], "A"),
        True,
    )
