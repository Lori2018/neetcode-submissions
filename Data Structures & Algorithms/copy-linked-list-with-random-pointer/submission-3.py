from collections import defaultdict

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node = head
        nodes = defaultdict(int)
        newNodes = defaultdict(Node)
        i = 0

        while node:
            i += 1
            nodes[node] = i
            newNodes[i] = Node(node.val, None, None)
            node = node.next
        
        node = head
        while node:
            cur = newNodes[nodes[node]]
            if node.next:
                cur.next = newNodes[nodes[node.next]]
            if node.random:
                cur.random = newNodes[nodes[node.random]]
            node = node.next

        return newNodes[nodes[head]] if nodes[head] else None
