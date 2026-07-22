class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])

        def add(i,j):
            if min(i,j) >= 0 and i < ROWS and j < COLS and grid[i][j] == 1:
                q.append((i,j))
                grid[i][j] = 2
                return True
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))

        time = 0
        while q:
            n = len(q)
            for x in range(n):
                i,j = q.popleft()
                add(i+1,j)
                add(i-1,j)
                add(i,j+1)
                add(i,j-1)
            if len(q) > 0:
                time += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return time