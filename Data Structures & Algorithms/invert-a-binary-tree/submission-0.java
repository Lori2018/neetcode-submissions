/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public TreeNode invertTree(TreeNode root) {
        invertNodes(root);
        return root;
    }

    public void invertNodes(TreeNode x) {
        if (x != null) {
            TreeNode temp = x.left;
            x.left = x.right;
            x.right = temp;
            invertNodes(x.left);
            invertNodes(x.right);
        }
    }
}
