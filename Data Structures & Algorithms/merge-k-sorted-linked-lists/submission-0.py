# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # get first min
        head = None
        minIndex = 0
        minVal = 1001

        for i in range(len(lists)):
            if lists[i] and lists[i].val < minVal:
                minVal = lists[i].val
                minIndex = i
        if minVal == 1001:
            return None

        head = lists[minIndex]
        lists[minIndex] = lists[minIndex].next

        head.next = self.mergeKLists(lists)
        return head