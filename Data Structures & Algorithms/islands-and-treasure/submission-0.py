class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs finds shortest distance
        # or use recursion -- grid[i][j] dist is 1 + min of 4 dirs
        n, m = len(grid[0]), len(grid)
        seen = [[0] * n for _ in range(m)]
        def dist(i,j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return math.inf
            if seen[i][j] == 1:
                return grid[i][j]
            if grid[i][j] == -1:
                return math.inf
            seen[i][j] = 1
            if grid[i][j] != 0:
                a, b, c, d = dist(i+1,j), dist(i,j+1), dist(i-1,j), dist(i,j-1)
                # print(f"{a},{b},{c},{d}")
                grid[i][j] = 1 + min(a,b,c,d, grid[i][j])
            # print(f"{i}, {j} returns {grid[i][j]}")
            return grid[i][j]
        
        # grid[0][0] = dist(0,0)
        for i in range(m):
            for j in range(n):
                # print(f"calling {i}, {j}")
                seen = [[0] * n for _ in range(m)]
                dist(i,j)
                print()