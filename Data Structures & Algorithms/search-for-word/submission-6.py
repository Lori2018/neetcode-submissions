class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) > len(board) * len(board[0]):
            return False
        boardCopy = None
        def dfs(x, y, index):
            if index >= len(word):
                return True
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] != word[index]:
                return False
            board[x][y] = "#"
            up = dfs(x,y+1,index+1)
            right = dfs(x+1,y,index+1)
            down = dfs(x,y-1,index+1)
            left = dfs(x-1,y,index+1)
            board[x][y] = word[index]
            return up or right or down or left

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False