# https://leetcode.com/problems/same-tree/
# 100. Same Tree


from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# O(n)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def _DFS(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val != q.val:
                return False

            if not _DFS(p.left, q.left):
                return False

            if not _DFS(p.right, q.right):
                return False

            return True

        return _DFS(p, q)


# O(n), 이게 맞게 푼 건가?
# 리스트화 해서 비교
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def _DFS(p: Optional[TreeNode]) -> List:
            if not p:
                return [None]
            res = []

            res.append(p.val)
            if p.left or p.right:
                res += _DFS(p.left)
                res += _DFS(p.right)

            return res

        pList = _DFS(p)
        qList = _DFS(q)

        print(pList)
        print(qList)

        return pList == qList
