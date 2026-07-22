import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # min heap of largest elems
        heap = []
        length = 0
        for num in nums:
            if length < k: 
                heapq.heappush(heap, num)
                length += 1
            elif heap[0] < num:
                heapq.heappushpop(heap, num)
        
        return heap[0]