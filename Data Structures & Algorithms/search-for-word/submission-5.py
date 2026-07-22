class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) > len(board) * len(board[0]):
            return False
        boardCopy = None
        def dfs(x, y, index):
            if index >= len(word):
                return True
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or boardCopy[x][y] != word[index]:
                return False
            boardCopy[x][y] = None
            up = dfs(x,y+1,index+1)
            if not up and y+1 < len(board[0]):
                boardCopy[x][y+1] = board[x][y+1]
            right = dfs(x+1,y,index+1)
            if not right and x+1 < len(board):
                boardCopy[x+1][y] = board[x+1][y]
            down = dfs(x,y-1,index+1)
            if not down and y-1 >= 0:
                boardCopy[x][y-1] = board[x][y-1]
            left = dfs(x-1,y,index+1)
            if not left and x-1 >= 0:
                boardCopy[x-1][y] = board[x-1][y]
            return up or right or down or left
        def copyBoard():
            copy = []
            for b in board:
                copy.append(b.copy())
            return copy
        for i in range(len(board)):
            for j in range(len(board[0])):
                boardCopy = copyBoard()
                if dfs(i,j,0):
                    return True
        return False