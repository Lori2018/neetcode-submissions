import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # put each stone into max heap 
        heap = []
        length = len(stones)

        for stone in stones:
            heapq.heappush(heap, stone * -1)
        
        while length > 1: 
            # pop heaviest
            x = heapq.heappop(heap) * -1
            y = heapq.heappop(heap) * -1
            length -= 2

            if x != y: 
                heapq.heappush(heap, (max(x,y) - min(x,y)) * -1)
                length += 1
        
        if length == 0:
            return 0
        
        return heapq.heappop(heap) * -1