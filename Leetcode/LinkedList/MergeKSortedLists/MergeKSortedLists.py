# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# O(m*n) 하나씩 합치기 반복
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
# for문으로 한번에 합치기
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
