# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/

from heapq import merge
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
공간 O(1) 해법
Heap을 쓰는 풀이는 Heap 폴더에 있음.
"""

# O(m*n) 머지 소트 186 ms
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        self.lists = lists
        return self.merge(0, len(lists) - 1)

    def merge(self, left: int, right: int) -> ListNode:
        if left > right:
            return None
        if left == right:
            return self.lists[left]

        mid = (left + right) // 2

        leftNode = self.merge(left, mid)
        rightNode = self.merge(mid + 1, right)

        return self.mergeLists(leftNode, rightNode)

    def mergeLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        head = ListNode()
        cur = head

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2

        return head.next


# O(m*n) 하나씩 합치기 반복 5359 ms
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        cur = head

        for list in lists:
            cur.next = self.mergeLists(cur.next, list)

        return head.next

    def mergeLists(self, list1, list2):
        head = ListNode()
        cur = head

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        if list1:
            cur.next = list1
        if list2:
            cur.next = list2

        return head.next


# O(m*n), m : length of Lists, n : length of linked-list
# for문으로 한번에 합치기 6828 ms
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        cur = head

        while any(lists):
            minVal = 10001
            num = -1
            for i, list in enumerate(lists):
                if not list:
                    continue
                if minVal > list.val:
                    minVal = list.val
                    num = i

            cur.next = lists[num]
            cur = cur.next
            lists[num] = lists[num].next

        return head.next
