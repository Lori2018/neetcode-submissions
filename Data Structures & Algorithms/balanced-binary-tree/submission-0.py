# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    heightBalanced = True 

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # get height of left and right subtrees
        self.getTreeHeight(root)
        return self.heightBalanced

    def getTreeHeight(self, node):
        if not node:
            return 0
        left = self.getTreeHeight(node.left)
        right = self.getTreeHeight(node.right)
        if abs(left - right) > 1:
            self.heightBalanced = False 
        return 1 + max(left, right)