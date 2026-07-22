# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # serialize 
        rootStr = self.serialize(root)
        subRootStr = self.serialize(subRoot)
        print(rootStr)
        print(subRootStr)
        print()

        for i in range(0, len(rootStr) - len(subRootStr) + 1):
            print(rootStr[i:i + len(subRootStr)])
            if rootStr[i:i + len(subRootStr)] == subRootStr:
                return True
        return False
        
    
    def serialize(self, node): 
        if not node: 
            return "#"
        else: 
            return "$" + str(node.val) + self.serialize(node.left) + self.serialize(node.right)
