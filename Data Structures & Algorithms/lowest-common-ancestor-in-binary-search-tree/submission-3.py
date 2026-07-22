# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque

class Solution:
    graph = defaultdict(list)
    nodes = defaultdict(TreeNode)
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if traveling from p to q, p must travel through LCA to get to q
        # build graph 
        # bfs from p until sees q and store all nodes in array
        # bfs from root & document heights - change val to heights

        # clear dicts 
        self.graph = defaultdict(list)
        self.nodes = defaultdict(TreeNode)
        # build graph 
        heights = self.buildGraph(root, 0)
        discovered = defaultdict()
        discovered[p.val] = True
        parent = defaultdict()
        queue = deque()
        queue.append(p.val)

        # bfs from p until discovers q
        while queue:
             node = queue.pop()
             for neighbor in self.graph[node]: 
                if neighbor not in discovered:
                    parent[neighbor] = node
                    if neighbor == q.val:
                        break
                    discovered[neighbor] = True 
                    queue.append(neighbor)
        
        # now traverse path from q to p through parent ptrs
        node = q.val
        minHeight = heights[node]
        lca = node

        while node != p.val: 
            if heights[node] < minHeight: 
                lca = node
                minHeight = heights[node]
            if node in parent:
                node = parent[node]
            else: 
                break
        if heights[node] < minHeight:
            lca = node
        return self.nodes[lca]

    def buildGraph(self, root, height):
        heights = defaultdict(int)
        if not root: 
            return heights
        heights[root.val] = height
        self.nodes[root.val] = root
        if root.left:
            self.graph[root.val] += [root.left.val]
            self.graph[root.left.val].append(root.val)
        if root.right:
            self.graph[root.val].append(root.right.val)
            self.graph[root.right.val].append(root.val)

        heightsLeft = self.buildGraph(root.left, height + 1)
        heightsRight = self.buildGraph(root.right, height + 1)
        heights.update(heightsLeft)
        heights.update(heightsRight)

        return heights

    def printDict(self, d):
        for key in d.keys(): 
            print(str(key) + ": " + str([item for item in d[key]]))
        