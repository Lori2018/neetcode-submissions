class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        queue = deque()
        x, y = len(grid), len(grid[0])

        for i in range(x):
            for j in range(y):
                if grid[i][j] == -1 or grid[i][j] == "0":
                    grid[i][j] = -1
                else:
                    res += 1
                    queue.append((i,j))
                    while len(queue) > 0: 
                        a,b = queue.popleft()
                        if a+1 < len(grid):
                            if grid[a+1][b] == "1":
                                queue.append((a+1,b))
                            grid[a+1][b] = -1
                        if b+1 < len(grid[0]):
                            if grid[a][b+1] == "1":
                                queue.append((a,b+1))
                            grid[a][b+1] = -1
                        if a-1 >= 0:
                            if grid[a-1][b] == "1":
                                queue.append((a-1,b))
                            grid[a-1][b] = -1
                        if b-1 >= 0:
                            if grid[a][b-1] == "1":
                                queue.append((a,b-1))
                            grid[a][b-1] = -1
        return res