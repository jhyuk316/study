package Tree.MaximumDepthOfBinaryTree;

import java.util.LinkedList;
import java.util.Queue;

// Definition for a binary tree node.
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {}

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}


class Solution {
    public int maxDepth(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();

        if (root == null) {
            return 0;
        }
        queue.add(root);

        int depth = 0;
        while (!queue.isEmpty()) {
            ++depth;
            Queue<TreeNode> tempQueue = new LinkedList<>();
            for (TreeNode tempNode : queue) {
                if (tempNode.left != null) {
                    tempQueue.add(tempNode.left);
                }
                if (tempNode.right != null) {
                    tempQueue.add(tempNode.right);
                }
            }
            queue = tempQueue;
        }

        return depth;
    }
}


public class MaximumDepthOfBinaryTree {
    public static void main(String[] args) {

    }
}
