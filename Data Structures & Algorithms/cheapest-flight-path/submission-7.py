import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [math.inf] * n
        dist[src] = 0

        for i in range(k+1):
            tmp = dist.copy()
            for frm, to, price in flights:
                if dist[frm] == math.inf:
                    continue
                if dist[frm] + price < tmp[to]:
                    tmp[to] = dist[frm] + price
            dist = tmp
            print(dist)
        return dist[dst] if dist[dst] != math.inf else -1

        
        
        # keep track of next airport
