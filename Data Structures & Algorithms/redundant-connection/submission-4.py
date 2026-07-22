class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        graph = defaultdict(list)
        cycle = set() 
        cycleStart = -1
        visit = set()

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # returns true if part of cycle, false otherwise
        def dfs(x, prev):
            nonlocal cycleStart
            if x in visit:
                cycleStart = x
                return True
            
            visit.add(x)
            for nei in graph[x]:
                if nei == prev:
                    continue
                if dfs(nei, x):
                    if cycleStart != -1:
                        cycle.add(x)
                    if x == cycleStart:
                        cycleStart = -1
                    return True
            return False

        dfs(1, -1)
        for u,v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]
        return []
                        