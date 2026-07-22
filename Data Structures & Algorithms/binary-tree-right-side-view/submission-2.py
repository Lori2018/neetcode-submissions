# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs and return last on each list
        if not root: 
            return []
        layers = [[root]]
        layerNum = 0 
        sol = []

        while len(layers[layerNum]) > 0: 
            layer = []
            for node in layers[layerNum]:
                if node.left:
                    layer.append(node.left)
                if node.right:
                    layer.append(node.right)
            sol.append(node.val)
            layers.append(layer)
            layerNum += 1
        
        return sol