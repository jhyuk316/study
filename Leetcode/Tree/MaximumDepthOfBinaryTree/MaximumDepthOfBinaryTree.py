# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/


from collections import deque
from typing import Deque, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n) BFS, top-down
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


# O(n) DFS, bottom-up
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


## TODO - 자체적으로 테스트 가능하게 만들기
if __name__ == "__main__":
    sol = Solution()

    tree1 = [3, 9, 20, None, None, 15, 7]

    head = TreeNode
    for i, val in enumerate(tree1):
        tempTree = TreeNode(val)
        tempTree.left = TreeNode(tree1[2 * i + 1])
        tempTree.right = TreeNode(tree1[2 * i + 1])

    print(sol.maxDepth())
    pass
