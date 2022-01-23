package Tree.InvertBinaryTree;
// 226. Invert Binary Tree
// https://leetcode.com/problems/invert-binary-tree/

// Definition for a binary tree node.
import Tree.TreeNode;
import java.util.Arrays;

// O(n)
class Solution {
    public TreeNode invertTree(TreeNode root) {
        return new TreeNode(root.val, _invertTree(root.right), _invertTree(root.left));
    }

    private TreeNode _invertTree(TreeNode root) {
        if (root == null) {
            return null;
        }

        if (root.left == null && root.right == null) {
            return new TreeNode(root.val);
        }

        return new TreeNode(root.val, _invertTree(root.right), _invertTree(root.left));
    }
}


public class InvertBinaryTree {
    public static void main(String[] args) {
        testSol(new TreeNode(new int[] {4, 2, 7, 1, 3, 6, 9}), new int[] {4, 7, 2, 9, 6, 3, 1});
    }

    static void testSol(TreeNode input, int[] out) {
        // todo : input, output match
        Solution sol = new Solution();
        // todo : solution match
        int[] res = sol.invertTree(input).toIntArray();
        if (Arrays.equals(res, out)) {
            System.out.println("O : " + res);
        } else {
            System.out.println("x : " + res + "	expect : " + out);
        }
    }
}
