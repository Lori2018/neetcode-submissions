# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper: 
    def __init__(self, node):
        self.node = node 
        
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
       # add all to heap 
        heap = []
        for l in lists:
            if l:
                print("add " + str(l.val))
                heapq.heappush(heap, NodeWrapper(l))
                l = l.next


        head = None
        cur = head
        while len(heap) > 0: 
            nodes = [heapq.heappop(heap).node]
            if not head:
                head = nodes[0]
            # print("popoped " + str(node.val))
            while len(heap) > 0 and heap[0] == nodes[0].val:
                nodes += [heapq.heappop(heap).node]
                print("added again")
            for node in nodes:
                if node.next: 
                    print("add " + str(node.next.val))
                    heapq.heappush(heap, NodeWrapper(node.next))
                if cur:
                    cur.next = node 
                cur = node 
        return head
            