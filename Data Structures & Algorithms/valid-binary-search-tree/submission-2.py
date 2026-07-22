# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return True
        return self.helper(root.left, -1001, root.val) and self.helper(root.right, root.val, 1001)
        
    def helper(self, node, minVal, maxVal):
        if not node: 
            return True
        if node.val >= maxVal or node.val <= minVal: 
            return False 
        return self.helper(node.left, minVal, node.val) and self.helper(node.right, node.val, maxVal)