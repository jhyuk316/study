package LinkedList.RemoveNthNodeFromEndOfList;
// 19. Remove Nth Node From End of List
// https://leetcode.com/problems/remove-nth-node-from-end-of-list/


// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;

    ListNode() {}

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}


// O(n) 해답: 빠른 포인터가 n만큼 가고
// 느린포인터와 빠른 포인터가 같이 전진.
// 빠른 포인터가 null이면 slow.next = slow.next.next
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        ListNode slow = dummy;
        ListNode fast = dummy;
        dummy.next = head;

        // Move fast in front so that the gap between slow and fast becomes n
        for (int i = 0; i < n + 1; i++) {
            fast = fast.next;
        }

        while (fast != null) {
            fast = fast.next;
            slow = slow.next;
        }

        slow.next = slow.next.next;
        return dummy.next;
    }
}


// O(n) 원형큐를 만들어서 순환하다 제거
class Solution1 {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode[] tempQueue = new ListNode[n + 1];
        int point = 0;

        ListNode dummy = new ListNode();
        dummy.next = head;
        ListNode cur = dummy;

        while (cur != null) {
            tempQueue[point] = cur;
            point = (point + 1) % (n + 1);
            cur = cur.next;
        }

        if (tempQueue[point] == null) {
            return null;
        } else if (tempQueue[(point + 1) % (n + 1)] != null) {
            tempQueue[point].next = tempQueue[(point + 1) % (n + 1)].next;
        }

        return dummy.next;
    }
}


public class RemoveNthNodeFromEndOfList {
    public static void main(String[] args) {

    }
}
