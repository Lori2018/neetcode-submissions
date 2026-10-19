# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # traverse to end of list with 2 pointers, one is n behind 
        l = r = head
        i = 0
        while r.next:
            if i >= n:
                l = l.next
            r = r.next
            i += 1
        if i ==n-1:
            return head.next
        temp = None
        if l.next:
            temp = l.next.next
        l.next = temp
        return head