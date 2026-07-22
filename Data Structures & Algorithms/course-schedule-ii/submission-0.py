class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build graph
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        # toposort

        q = deque() 
        res = []
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        while q:
            p = q.popleft() 
            for out in graph[p]:
                indegree[out] -= 1
                if indegree[out] == 0:
                    q.append(out)
            res.append(p)
        
        if len(res) != numCourses:
            return []
        return res
            
