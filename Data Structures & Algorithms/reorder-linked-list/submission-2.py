# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def printList(node):
            l = []
            while node:
                l.append(node.val)
                node = node.next
            print(l)

        def reverse(node):
            # 1 2 3 4 
            # 4 3 2 1
            prev = None
            cur = node
            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev
        
        elem = tail = head
        n = 0
        while tail.next:
            tail = tail.next
            n += 1
        if n == 0:
            return
        counter = 0
        cur = head
        prev = None
        while counter < math.ceil(n/2):
            counter += 1
            prev = cur
            cur = cur.next
        prev.next = None

        nodeA = head
        nodeB = reverse(cur)
        printList(nodeA)
        printList(nodeB)
        
        # now we have 2 lists: head, cur (to be inserted)
        # reverse order of second half list -> 10, 8
        while nodeA and nodeB:
            tempA = nodeA.next
            tempB = nodeB.next
            nodeA.next = nodeB
            if tempA:
                nodeB.next = tempA
            nodeA = tempA
            nodeB = tempB