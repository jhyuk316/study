# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        temp = f"{self.val}"
        nextNode = self.next
        while nextNode is not None:
            temp += f", {nextNode.val}"
            nextNode = nextNode.next
        return temp


def makeCycleList(list: List[int], pos: int) -> ListNode:
    tempList = ListNode(0)
    result = tempList

    cycleNode = None
    for i, val in enumerate(list):
        tempNode = ListNode(val)
        if pos == i:
            cycleNode = tempNode
        tempList.next = tempNode
        tempList = tempList.next
    tempNode.next = cycleNode

    return result.next


# speed: O(n), space: O(1)
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            slow = head
            fast = head.next
        except:
            return False

        while slow and fast:
            if slow == fast:
                return True
            try:
                slow = slow.next
                fast = fast.next.next
            except:
                return False
        return False


# speed: O(n), space: O(n)
class Solution1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        address = set()
        while head:
            if id(head) in address:
                return True
            else:
                address.add(id(head))
            head = head.next
        return False


if __name__ == "__main__":
    sol = Solution()
    a = makeCycleList([1, 2, 3, 4, 5], 1)
    print(sol.hasCycle(a))
    b = makeCycleList([1], -1)
    print(sol.hasCycle(b))
