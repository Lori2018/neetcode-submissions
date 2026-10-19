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
        # hash map of oldNode to newNode
        # first pass: make copy of nodes and hash map
        newNodes = {None: None}
        cur = head
        while cur:
            newNodes[cur] = Node(cur.val)
            cur = cur.next
        # copy pointers
        cur = head
        curNew = newNodes[head]
        prev = None
        prevNew = None
        while cur:
            if prevNew:
                prevNew.next = newNodes[cur]
            if cur.random:
                newNodes[cur].random = newNodes[cur.random]
            if cur.next:
                newNodes[cur].next = newNodes[cur.next]
            cur = cur.next

        return newNodes[head]