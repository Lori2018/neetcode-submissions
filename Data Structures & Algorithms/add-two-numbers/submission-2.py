# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l = l1
        r = l2
        cur = None
        prev = None
        head = None
        carry = 0

        while l or r:
            # print(l.val + r.val + carry)
            if l and r:
                sum = l.val + r.val + carry
            elif l: 
                sum = l.val + carry
            else: 
                sum = r.val + carry
            cur = ListNode(sum, None)
            if cur.val >= 10:
                cur.val = cur.val % 10 
                carry = 1
            else: 
                carry = 0
            if not prev:
                head = cur
            if prev:
                prev.next = cur
            prev = cur
            if l:
                l = l.next
            if r:
                r = r.next
        if carry > 0: 
            cur.next = ListNode(carry, None)

        return head
            
