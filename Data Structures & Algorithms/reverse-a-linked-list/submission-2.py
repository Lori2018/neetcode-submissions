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
        while n:
            temp = n.next
            n.next = prev 
            prev = n
            n = temp 
        return prev