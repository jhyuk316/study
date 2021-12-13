package LinkedList.ReverseLinkedList;
// 206. Reverse Linked List
// https://leetcode.com/problems/reverse-linked-list/

import java.util.LinkedList;
import java.util.List;

// * Definition for singly-linked list.
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

    @Override
    public String toString() {
        String temp = String.valueOf(this.val);
        ListNode next = this.next;
        while (next != null) {
            temp += ", " + next.val;
            next = next.next;
        }
        return temp;
    }
}


// O(n)
class Solution {
    public ListNode reverseList(ListNode head) {
        return _reverseList(head, null);
    }

    private ListNode _reverseList(ListNode head, ListNode prev) {
        if (head == null) {
            return prev;
        }

        ListNode next = head.next;
        head.next = prev;

        return _reverseList(next, head);
    }
}


// O(n)
class Solution2 {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        while (head != null) {
            ListNode curr = head;
            head = head.next;
            curr.next = prev;
            prev = curr;
        }

        return prev;
    }
}


// O(n)
class Solution1 {
    public ListNode reverseList(ListNode head) {
        if (head == null) {
            return null;
        }

        ListNode result = new ListNode();

        ListNode it = head;
        while (it.next != null) {
            ListNode temp = new ListNode(it.val);

            temp.next = result.next;
            result.next = temp;

            it = it.next;
        }
        result.val = it.val;

        return result;
    }
}


public class ReverseLinkedList {
    public static void main(String[] args) {
        LinkedList list = new LinkedList();

        ListNode head = new ListNode(1);
        ListNode next = head;
        while (next.next != null)
            next = next.next;
        for (int i = 2; i <= 5; ++i) {
            ListNode temp = new ListNode(i);
            next.next = temp;
            next = next.next;
        }

        System.out.println(head);

        Solution sol = new Solution();

        System.out.println(sol.reverseList(head));
    }

}
