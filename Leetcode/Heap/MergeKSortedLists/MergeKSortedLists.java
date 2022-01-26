package Heap.MergeKSortedLists;
// 23. Merge k Sorted Lists
// https://leetcode.com/problems/merge-k-sorted-lists/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;
// Definition for singly-linked list.
import LinkedList.ListNode;


// 리스트 저장 후 정렬, 9ms
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        List<ListNode> tempList = new ArrayList<>();

        for (ListNode head : lists) {
            while (head != null) {
                tempList.add(head);
                head = head.next;
            }
        }

        tempList.sort(Comparator.comparing(node -> node.val));
        // tempList.sort((a, b) -> ((Integer) a.val).compareTo((Integer) b.val));
        // tempList.sort((a, b) -> a.val - b.val);

        for (int i = 0; i < tempList.size() - 1; ++i) {
            tempList.get(i).next = tempList.get(i + 1);
        }

        if (tempList.size() == 0) {
            return null;
        }

        tempList.get(tempList.size() - 1).next = null;
        return tempList.get(0);
    }
}


// minHeap 저장. 10ms
class Solution1 {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> minHeap =
                new PriorityQueue<>(Comparator.comparing(node -> node.val));

        for (ListNode head : lists) {
            while (head != null) {
                minHeap.add(head);
                head = head.next;
            }
        }

        ListNode head = minHeap.poll();
        ListNode cur = head;
        while (!minHeap.isEmpty()) {
            cur.next = minHeap.poll();
            cur = cur.next;
        }

        if (cur != null) {
            cur.next = null;
        }

        return head;
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
