package LinkedList.MergeKSortedLists;
// 23. Merge k Sorted Lists
// https://leetcode.com/problems/merge-k-sorted-lists/

import java.util.Arrays;
// Definition for singly-linked list.
import LinkedList.ListNode;


// 분할 머지 빠름 3ms.
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        return merge(lists, 0, lists.length - 1);
    }

    private ListNode merge(ListNode[] lists, int left, int right) {
        if (left > right) {
            return null;
        }
        if (left == right) {
            return lists[left];
        }

        int mid = (left + right) / 2;

        ListNode leftNode = merge(lists, left, mid);
        ListNode rightNode = merge(lists, mid + 1, right);

        return mergeLists(leftNode, rightNode);
    }

    private ListNode mergeLists(ListNode node1, ListNode node2) {
        ListNode head = new ListNode();
        ListNode dummy = head;

        while (node1 != null && node2 != null) {
            if (node1.val <= node2.val) {
                dummy.next = node1;
                node1 = node1.next;
            } else {
                dummy.next = node2;
                node2 = node2.next;
            }
            dummy = dummy.next;
        }

        if (node1 != null) {
            dummy.next = node1;
        } else if (node2 != null) {
            dummy.next = node2;
        }

        return head.next;
    }
}


// 단순하게 앞에서부터 머지 느림 248ms.
class Solution1 {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0)
            return null;

        ListNode dummy = null;
        for (ListNode node : lists) {
            dummy = mergeLists(dummy, node);
        }

        return dummy;
    }

    private ListNode mergeLists(ListNode node1, ListNode node2) {
        ListNode head = new ListNode();
        ListNode dummy = head;

        while (node1 != null && node2 != null) {
            if (node1.val <= node2.val) {
                dummy.next = node1;
                node1 = node1.next;
            } else {
                dummy.next = node2;
                node2 = node2.next;
            }
            dummy = dummy.next;
        }

        if (node1 != null) {
            dummy.next = node1;
        } else if (node2 != null) {
            dummy.next = node2;
        }

        return head.next;
    }
}


public class MergeKSortedLists {
    public static void main(String[] args) {
        testSol(new ListNode[] {new ListNode(new int[] {1, 4, 5}),
                new ListNode(new int[] {1, 3, 4}), new ListNode(new int[] {2, 6})},
                new int[] {1, 1, 2, 3, 4, 4, 5, 6});
        testSol(new ListNode[] {}, null);
    }

    static void testSol(ListNode[] input, int[] output) {
        Solution sol = new Solution();
        // todo : solution match
        ListNode temp = sol.mergeKLists(input);
        int[] res = temp != null ? temp.toIntArrays() : null;
        if (Arrays.equals(res, output)) {
            System.out.println("O : " + res);
        } else {
            System.out.println("x : " + res + "	expect : " + output);
        }
    }
}
