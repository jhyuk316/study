# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/

import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
자료구조를 사용하는 풀이
공간 O(1) 해법은 linkedList폴더에 있음.
"""

# O(m*n) list 104 ms. heapq 더럽다.
# 자바와 달리 다른 모듈을 불러오는게 느낌이 좋지 않음.
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodeList = []

        count = 0
        for i, node in enumerate(lists):
            while node:
                count += 1
                # node.val을 비교하고 count를 비교하고 node를 비교해서 heap에 넣음.
                # 유일한 값이 아니면 node끼리 비교하려고하는데 이에 실패해서 에러남.
                heapq.heappush(nodeList, (node.val, count, node))
                node = node.next

        head = prev = ListNode()
        while nodeList:
            prev.next = heapq.heappop(nodeList)[2]
            prev = prev.next

        return head.next


# O(m*n) list 84 ms. 이게 이렇게 빨라?
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodeList = []

        for node in lists:
            while node:
                nodeList.append(node)
                node = node.next

        nodeList.sort(key=lambda x: x.val)

        head = cur = ListNode()
        for node in nodeList:
            cur.next = node
            cur = cur.next
        cur.next = None
        return head.next
