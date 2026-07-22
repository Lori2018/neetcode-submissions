import heapq
import math
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dijikstra
        graph = defaultdict(list)
        for ui, vi, ti in times:
            graph[ui].append((vi, ti))
        heap = [(0,k)]
        visit = set()
        t = 0

        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in visit:
                continue
            t = w1

            for n2, w2 in graph[n1]:
                if n2 not in visit:
                    heapq.heappush(heap, (w1+w2, n2))
            visit.add(n1)
        return t if len(visit) == n else -1