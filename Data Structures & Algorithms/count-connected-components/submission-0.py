class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visit = set() 
        res = 0

        def dfs(x):
            if x in visit:
                return 
            visit.add(x)
            for neighbor in graph[x]:
                dfs(neighbor)
        
        for i in range(n):
            if i not in visit:
                dfs(i)
                res += 1
        
        return res