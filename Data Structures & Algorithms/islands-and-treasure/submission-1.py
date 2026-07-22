class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs finds shortest distance
        # or use recursion -- grid[i][j] dist is 1 + min of 4 dirs
        n, m = len(grid[0]), len(grid)
        seen = [[0] * n for _ in range(m)]
        def dist(i,j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == -1:
                return math.inf
            if seen[i][j] == 1:
                return grid[i][j]
            seen[i][j] = 1
            grid[i][j] = min(dist(i+1,j), dist(i,j+1), dist(i-1,j), dist(i,j-1), grid[i][j]) + (1 if grid[i][j] != 0 else 0)
            return grid[i][j]
        
        for i in range(m):
            for j in range(n):
                seen = [[0] * n for _ in range(m)]
                dist(i,j)
                print()