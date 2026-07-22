# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # kth from left to right
        # do an inorder traversal 
        arr = self.getInorder(root) 
        return arr[k - 1]

    def getInorder(self, node): 
        if not node: 
            return []
        else: 
            return self.getInorder(node.left) + [node.val] + self.getInorder(node.right)