# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

"""
Linked List 조작은 너무 어렵다. 외워야겠다.
포인터가 없으니 포인터를 가르키는 지 객체를 가르키는 지 너무 모호함. ㅠ.ㅠ
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        temp = ""
        next = self.next
        while next:
            temp += " " + str(next.val)
            next = next.next
        return temp


# O(m+n)
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode()  # 리턴할 헤더
        cur = head  # 작업할 커서

        # Merge
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        # 나머지
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2

        return head.next
