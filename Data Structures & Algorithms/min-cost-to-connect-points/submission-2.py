import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        coords = {}
        i = 0
        for x1,y1 in points:
            coords[i] = [x1, y1]
            i += 1
            
        for c in coords.keys():
            for j in range(i+1):
                if c != j:
                    graph[c].append(j)
        
        heap = [(0, 0)]
        for i in range(1, len(points)):
            heapq.heappush(heap, (10000000, i))
        res = 0
        while len(heap) > 0:
            distance, x = heapq.heappop(heap)
            res += distance

            # update all distances
            for i in range(len(heap)):
                d, node = heap[i]
                heap[i] = (min(d, abs(coords[x][0]-coords[node][0]) + abs(coords[x][1]-coords[node][1])), node)
            heapq.heapify(heap)
            
        return res