class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visit = set()
        ROWS, COLS = len(board), len(board[0])
        def bfs(i, j):
            q = deque()
            v = set()
            q.append((i,j))
            v.add((i,j))

            while q:
                x,y = q.popleft()
                if x-1 >= 0: 
                    if (x-1,y) not in v and board[x-1][y] == "O":
                        q.append((x-1,y))
                        v.add((x-1,y))
                else:
                    visit.union(v)
                    return 
                if y-1 >= 0:
                    if (x,y-1) not in v and board[x][y-1] == "O":
                        q.append((x,y-1))
                        v.add((x,y-1))
                else:
                    visit.union(v)
                    return 
                if x+1 < ROWS:
                    if (x+1,y) not in v and board[x+1][y] == "O":
                        q.append((x+1,y))
                        v.add((x+1,y))
                else:
                    visit.union(v)
                    return
                if y+1 < COLS:
                    if (x,y+1) not in v and board[x][y+1] == "O":
                        q.append((x,y+1))
                        v.add((x,y+1))
                else:
                    visit.union(v)
                    return 
            
            for x,y in v:
                board[x][y] = "X"
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    bfs(i,j)
        