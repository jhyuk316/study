# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# O(n)
class Solution:
    listNode = [None] * 101  # static 변수

    def cloneGraph(self, node: "Node") -> "Node":
        if not node:
            return None

        if node.val == 1:
            self.listNode = [None] * 101

        # print(node.val)
        tempNode = Node(node.val)
        self.listNode[node.val] = tempNode

        for neighbor in node.neighbors:
            # print(f"node {node.val}, ne.val {neighbor.val}")
            if self.listNode[neighbor.val]:
                tempNode.neighbors.append(self.listNode[neighbor.val])
            else:
                tempNode.neighbors.append(self.cloneGraph(neighbor))

        return tempNode
