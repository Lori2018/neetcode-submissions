# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# a <- temp  temp2
# a <- b <- c

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = head 
        prev = None 
        if n:
            while n.next:
                temp = n 
                n = n.next 
                temp.next = prev 
                prev = temp 
            n.next = prev
        return n