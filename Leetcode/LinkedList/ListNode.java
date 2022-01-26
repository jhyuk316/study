package LinkedList;

import java.nio.BufferOverflowException;
import java.util.ArrayList;
import java.util.List;

public class ListNode {
    public int val;
    public ListNode next;

    public ListNode() {}

    public ListNode(int val) {
        this.val = val;
    }

    public ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }

    public ListNode(int[] vals) {
        this.val = vals[0];
        if (vals.length > 1) {
            this.next = _ListNode(vals, 1);
        }
    }

    private ListNode _ListNode(int[] vals, int index) {
        if (vals.length == index) {
            return null;
        }
        return new ListNode(vals[index], _ListNode(vals, index + 1));
    }

    public int[] toIntArrays() {
        if (hasCycle()) {
            throw new BufferOverflowException();
            // return new int[] {};
        }

        List<Integer> valList = new ArrayList<>();
        valList.add(this.val);
        ListNode cur = this.next;
        while (cur != null) {
            valList.add(cur.val);
            cur = cur.next;
        }

        return valList.stream().mapToInt(i -> i).toArray();
    }

    public boolean hasCycle() {
        ListNode slow = this;
        ListNode fast = this;

        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) {
                return true;
            }
        }
        return false;
    }

}
