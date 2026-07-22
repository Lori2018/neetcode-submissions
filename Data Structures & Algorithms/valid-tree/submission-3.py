class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # construct graph 
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visit = set()
        def dfs(x, prev):
            if x in visit:
                return False
            visit.add(x)
            for i in graph[x]:
                if i == prev:
                    continue
                if not dfs(i, x):
                    return False
            return True
        return dfs(0, -1) and len(visit) == n