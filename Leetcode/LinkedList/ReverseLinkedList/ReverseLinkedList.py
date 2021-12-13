#  206. Reverse Linked List
#  https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
from typing import Counter, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        temp = f"{self.val}"
        nextNode = self.next
        while nextNode is not None:
            temp += f", {nextNode.val}"
            nextNode = nextNode.next
        return temp


# recursively
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self._reverseList(head, None)

    def _reverseList(self, head: Optional[ListNode], prev: Optional[ListNode]):
        if head is None:
            return prev

        next = head.next
        head.next = prev
        return self._reverseList(next, head)


# iteratively
class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr

        return prev


if __name__ == "__main__":
    sol = Solution()

    head = ListNode(1)
    nextNode = head
    for i in range(2, 6):
        temp = ListNode(i)
        nextNode.next = temp
        nextNode = nextNode.next

    print(f"head: {head}")

    result: ListNode = sol.reverseList(head)
    print(f"result: {result}")
    # result: ListNode = sol.reverseList(ListNode())
    # print(f"result: {result}")
