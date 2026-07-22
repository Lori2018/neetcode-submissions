class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # b before a
        graph = defaultdict(list)
        res = True
        color = [0] * numCourses
        for a,b in prerequisites:
            graph[b].append(a)
        print(graph)
        # dfs and find backedge
        def dfs(x):
            nonlocal res
            color[x] = 1
            print(color)
            for i in graph[x]:
                if color[i] == 1:
                    res = False
                else:
                    dfs(i)
            color[x] = 2

        for i in range(numCourses):
            if color[i] == 0:
                dfs(i)
        return res