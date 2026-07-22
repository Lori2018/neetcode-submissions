from collections import Counter, defaultdict
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # do largest first 
        # maxheap keyed on frequency
        counts = Counter(tasks)
        heap = []
        for c in counts.items():
            heapq.heappush(heap, (-1 * c[1], c[0]))
        
        res = 0
        waiting = defaultdict(list)
        waitingLength = 0
        while heap or waitingLength > 0:
            waitingLength -= len(waiting[res])
            for w in waiting[res]:
                heapq.heappush(heap, w)
            if len(heap) > 0:
                i = heapq.heappop(heap)
                if i[0] < -1:
                    waiting[res + n + 1].append((i[0] + 1, i[1]))
                    waitingLength += 1
            res += 1
            # print(heap)
        return res