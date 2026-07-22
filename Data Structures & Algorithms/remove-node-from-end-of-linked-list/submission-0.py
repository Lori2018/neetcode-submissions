# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
         # two pointers that are n + 1 away
        # when you hit the end, rm the lo ptr
        lo = head
        prev = None 
        hi = head
        dist = 0 
        while hi.next: 
            if dist < n - 1:
                dist += 1
            else: 
                prev = lo
                lo = lo.next
            hi = hi.next

        # remove lo ptr
        if prev:
            prev.next = lo.next
        else: 
            # node is head of list 
            return lo.next
            # return lo if lo != hi else None

        return head
