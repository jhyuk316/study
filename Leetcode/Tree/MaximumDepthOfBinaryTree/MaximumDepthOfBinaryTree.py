# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/


from collections import deque
from typing import Deque, List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n) BFS, bottom-up? top-down? 따지고 보면 후치 연산 아닌가?
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        nodeQueue: Deque[TreeNode] = deque()
        count = 0

        if root:
            nodeQueue.append(root)

        while nodeQueue:
            tempQueue = deque()
            while nodeQueue:
                node: TreeNode = nodeQueue.popleft()
                if node.left:
                    tempQueue.append(node.left)
                if node.right:
                    tempQueue.append(node.right)

            nodeQueue = tempQueue
            count += 1

        return count


# 이렇게 짜도 과연 괜찮은 것인가? ㅋㅋㅋ
# java에서 해봤더니 ConcurrentModificationException 발생.
class Solution3:
    def maxDepth(self, root):
        if not root:
            return 0

        queue = [root]
        depth = 0
        while queue:
            depth += 1
            # list는 for 내부에서 변경해도 for문이 바뀌지 않음.
            for node in queue:
                queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return depth


# O(n) DFS, bottom-up
class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1


# O(n) DFS, top-down
class Solution1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            return self._maxDepth(root, 1)
        return 0

    def _maxDepth(self, root: Optional[TreeNode], depth: int) -> int:
        print(root.val, depth)
        if not root.left and not root.right:
            return depth

        left = 0
        right = 0

        if root.left:
            left = self._maxDepth(root.left, depth + 1)

        if root.right:
            right = self._maxDepth(root.right, depth + 1)

        return max(left, right)


def testSol(func, input, output):
    res = func(input)
    if res == output:
        print(f"O : {res}")
    else:
        print(f"X : {res}	excpet : {output}")


if __name__ == "__main__":
    sol = Solution()

    def makeTree(tree: List[int], pos: int = 0) -> TreeNode:
        if pos >= len(tree):
            return None

        node = TreeNode(tree[pos])
        node.left = makeTree(tree, 2 * pos + 1)
        node.right = makeTree(tree, 2 * pos + 2)

        return node

    testSol(sol.maxDepth, makeTree([3, 9, 20, None, None, 15, 7]), 3)
    testSol(sol.maxDepth, makeTree([1, None, 2]), 2)
    testSol(
        sol.maxDepth,
        makeTree([1, 2, 3, 4, 5, 6, None, None, None, None, None, 7, 8]),
        4,
    )
