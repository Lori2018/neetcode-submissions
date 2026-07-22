# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        count = 1
        node = head
        while node.next:
            count += 1
            node = node.next

        nodes = [None] * ((count - 1) // 2)
        # iterate through linked list again to get switch nodes 
        node = head 
        i = 1
        ptr = 0
        end = None
        while node.next:            
            if count - i <= (count - 1) // 2: 
                temp = node
                nodes[(len(nodes) - 1) - ptr] = node
                ptr += 1
                node = node.next
                if ptr == 1:
                    end = temp 
            else: 
                node = node.next
            i += 1
        
        # verify correct nodes were gotten
        lo = head
        for n in nodes:
            node = n.next
            print("trying to do " + str(lo.val) + " then " + str(node.val))
            temp = lo.next
            lo.next = node
            node.next = temp
            lo = temp
        
        if end:
            end.next = None