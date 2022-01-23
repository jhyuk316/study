package Tree;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;

    public TreeNode() {}

    public TreeNode(int val) {
        this.val = val;
    }

    public TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }

    public TreeNode(int[] vals) {
        this.val = vals[0];
        if (1 < vals.length) {
            this.left = _TreeNode(vals, 1);
        }
        if (2 < vals.length) {
            this.right = _TreeNode(vals, 2);
        }
    }

    private TreeNode _TreeNode(int[] vals, int i) {
        TreeNode temp = new TreeNode(vals[i]);
        if ((i * 2 + 1) < vals.length) {
            temp.left = _TreeNode(vals, i * 2 + 1);
        }
        if ((i * 2 + 2) < vals.length) {
            temp.right = _TreeNode(vals, i * 2 + 2);
        }
        return temp;
    }

    public int[] toIntArray() {
        List<Integer> result = new ArrayList<>();
        result.add(this.val);

        Queue<TreeNode> bfs = new LinkedList<>();
        if (this.left != null) {
            bfs.add(this.left);
        }
        if (this.right != null) {
            bfs.add(this.right);
        }

        while (!bfs.isEmpty()) {
            TreeNode temp = bfs.poll();
            result.add(temp.val);

            if (temp.left != null) {
                bfs.add(temp.left);
            }
            if (temp.right != null) {
                bfs.add(temp.right);
            }
        }

        return result.stream().mapToInt(i -> i).toArray();
    }
}
