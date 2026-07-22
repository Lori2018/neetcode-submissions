# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # bfs and get leaf in lowest level 
        # bfs from leaf and return # levels
        layers = [[root]]
        layer = 0 
        n = None
        graph = defaultdict(list)

        while len(layers[layer]) > 0:
            layers += [[]]
            for node in layers[layer]:
                n = node
                if node.left: 
                    graph[node.left] += [node]
                    graph[node] += [node.left]
                    layers[layer + 1] += [node.left]
                if node.right:
                    graph[node.right] += [node]
                    graph[node] += [node.right]
                    layers[layer + 1] += [node.right]                
            layer += 1
        # n will be lowest leaf 
        # now bfs from n 
        layers = [[n]]
        layer = 0 
        length = 0
        discovered = defaultdict()
        discovered[n] = 1

        while len(layers[layer]) > 0:
            layers += [[]]
            for node in layers[layer]:
                for i in graph[node]:
                    if i not in discovered:
                        layers[layer + 1] += [i]    
                        discovered[i] = 1
            layer += 1
            length += 1
        layers = layers[:-1]
        return length - 1
