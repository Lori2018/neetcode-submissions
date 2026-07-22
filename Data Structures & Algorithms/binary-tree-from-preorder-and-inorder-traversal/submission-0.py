# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    indices = {}
    index = 0
    lst = []
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        for i in range(len(inorder)):
            self.indices[inorder[i]] = i
        self.lst = preorder
        
        return self.helper(0, len(self.lst) - 1)
    
    def helper(self, lo, hi):
        if self.index >= len(self.lst):# or hi < 0 or lo >= len(self.lst): 
            return None 
        print("called on " + str(self.lst[self.index]) + ", " + str(lo) + " " + str(hi))
        inorderVal = self.indices[self.lst[self.index]]
        print(inorderVal)
        if inorderVal < lo or inorderVal > hi: 
            print("return NONE")
            return None
        node = TreeNode(self.lst[self.index], None, None)
        self.index += 1
        node.left = self.helper(0, max(0, inorderVal - 1))
        # self.index += 1
        print("calling right")
        node.right = self.helper(min(hi, inorderVal + 1), hi)
        print("done calling right")

        return node




