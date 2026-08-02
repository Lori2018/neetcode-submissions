# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def rec(root, cur):
            if not cur: # if at end, return root
                return root
            root = rec(root, cur.next)
            if not root:
                return None
            # stopping cases
            tmp = None
            if root == cur or root.next == cur:
                cur.next = None # make sure we don't do entire loop
            else:
                # suppose we're doing a reordering: 
                tmp = root.next
                root.next = cur
                cur.next = tmp
            return tmp
        rec(head, head.next)