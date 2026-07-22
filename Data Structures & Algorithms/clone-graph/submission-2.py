"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # make array of nodes
        # must dfs
        if node:
            root = Node(node.val)
        else:
            return None

        nodes = {}
        processed = [0] * 100

        queue = deque()
        nodes[node.val] = Node(node.val)
        queue.append(node)

        while len(queue) > 0:
            n = queue.pop() 
            print(n.val)
            if processed[n.val-1] == 1:
                continue
            processed[n.val-1] = 1
            for neighbor in n.neighbors:
                if neighbor.val not in nodes:
                    nodes[neighbor.val] = Node(neighbor.val)
                nodes[n.val].neighbors.append(nodes[neighbor.val])
                queue.append(neighbor)
        
        return nodes[node.val]
                
