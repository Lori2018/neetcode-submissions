class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid[0]), len(grid)
        
        def bfs(i,j):
            area = 1
            queue = deque() 
            queue.append((i,j))
            while len(queue) > 0:
                a,b = queue.pop()
                print(f"{a}, {b}")
                if a+1 < m and grid[a+1][b] == 1:
                    grid[a+1][b] = -1
                    area += 1
                    queue.append((a+1,b))
                if b+1 < n and grid[a][b+1] == 1:
                    grid[a][b+1] = -1
                    area += 1
                    queue.append((a,b+1))
                if a-1 >= 0 and grid[a-1][b] == 1:
                    grid[a-1][b] = -1
                    area += 1
                    queue.append((a-1,b))
                if b-1 >= 0 and grid[a][b-1] == 1:
                    grid[a][b-1] = -1
                    area += 1
                    queue.append((a,b-1))
            return area
        
        res = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = -1
                    res = max(res, bfs(i,j))
        return res