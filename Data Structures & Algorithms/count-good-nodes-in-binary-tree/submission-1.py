# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.helper(root, root.val)

    def helper(self, node, maxVal): 
        count = 0
        if not node: 
            return 0
        if node.val >= maxVal: 
            count += 1 
        return count + self.helper(node.left, max(node.val, maxVal)) + self.helper(node.right, max(node.val, maxVal))