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
    public int maxDepth(TreeNode root) {
        return getDepth(root, 0);
    }

    public int getDepth(TreeNode n, int curLength) {
        if (n != null) {
            int left = getDepth(n.left, curLength + 1);
            int right = getDepth(n.right, curLength + 1);
            return left > right ? left : right;
        } else {
            return curLength;
        }
    }
}
