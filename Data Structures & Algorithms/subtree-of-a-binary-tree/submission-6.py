# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isSameTree(root, subRoot): 
            return True 
        else: 
            print("root is not same tree")
            left = False
            right = False
            if root.left:
                left = self.isSubtree(root.left, subRoot)
            if root.right: 
                right = self.isSubtree(root.right, subRoot)
            return left or right

    def isSameTree(self, root, subRoot): 
        if not root and not subRoot: 
            return True
        if not root or not subRoot or root.val != subRoot.val: 
            print("return false")
            return False 
        if not root.left and not root.right and not subRoot.left and not subRoot.right: 
            return root.val == subRoot.val
        
        else: 
            print("checking " + str(root.val) + " " + str(subRoot.val))
            print("return true")
            return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)