# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/

"""
그래프를 만들고 사이클이 있는지 판단 하는 문제.
그래프는 링크드 리스트나 매트릭스로 만들 수 있을 듯.
루트를 알 수 있을까? 참조 되지 않는 노드? 알 수 없었음.
모든 노드를 돌지만, 루프가 아닌 노드들을 전부 끊어서 시간 단축.
"""

from typing import List

# O(n)?
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.mat = [[] for _ in range(numCourses)]
        for (a, b) in prerequisites:
            self.mat[a].append(b)

        self.visited = [False] * numCourses
        for i in range(numCourses):
            # print("\nstart ", i)
            if self.hasCycle(i):
                return False

        return True

    def hasCycle(self, node):
        # print(node, "->", end=" ")
        if not self.mat[node]:
            return False

        if self.visited[node] == True:
            return True

        self.visited[node] = True

        for next in self.mat[node]:
            if self.hasCycle(next):
                return True
            else:
                if next in self.mat[node]:
                    self.mat[node].remove(next)
            self.visited[next] = False

        self.visited[node] = False
        return False


if __name__ == "__main__":
    sol = Solution()

    print(sol.canFinish(5, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 2]]))
    print(sol.canFinish(2, [[1, 0]]))
    print(sol.canFinish(2, [[1, 0], [0, 1]]))
    print(sol.canFinish(4, [[2, 1], [1, 2], [1, 0], [3, 1], [2, 0], [3, 2]]))
    print(sol.canFinish(4, [[2, 1], [1, 0], [3, 1], [2, 0], [3, 2]]))
    print(sol.canFinish(4, [[2, 1], [3, 1], [1, 0], [2, 0]]))
    print(sol.canFinish(4, [[2, 1], [3, 1], [1, 0], [2, 0], [0, 3]]))
    print(sol.canFinish(5, [[2, 0], [0, 1], [4, 3], [3, 2]]))
