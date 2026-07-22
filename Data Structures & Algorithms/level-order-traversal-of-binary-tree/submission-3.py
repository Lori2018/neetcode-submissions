# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        layers = [[root]]
        layerNum = 0 

        while len(layers[layerNum]) > 0:
            layer = []
            for node in layers[layerNum]:
                if node.left:
                    layer.append(node.left)
                if node.right:
                    layer.append(node.right)
            layers.append(layer)
            layerNum += 1

        return [[node.val for node in layer] for layer in layers][:-1]