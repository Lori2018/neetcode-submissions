import math 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # store (dist, point) on heap
        # max heap
        heap = []
        length = 0

        for point in points:
            dist = math.sqrt(pow(point[0],2) + pow(point[1], 2))
            if length < k:
                heapq.heappush(heap, (dist * -1, point))
                length += 1
            elif dist < heap[0][0] * -1:
                heapq.heappushpop(heap, (dist * -1, point))

        return [h[1] for h in heap]