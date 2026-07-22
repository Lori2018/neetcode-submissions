class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkRow(row):
            p = [False for _ in range(10)]
            for i in range(9):
                num = None if board[row][i] == "." else int(board[row][i])
                if not num:
                    continue
                if p[num]:
                    return False
                p[num] = True
            return True
        def checkCol(col):
            p = [False for _ in range(10)]
            for i in range(9):
                num = None if board[i][col] == "." else int(board[i][col])
                if not num:
                    continue
                if p[num]:
                    return False
                p[num] = True
            return True
        def checkBox(box):
            p = [False for _ in range(10)]
            row_range = []
            col_range = []
            if box % 3 == 0:
                col_range = [0, 1, 2]
            elif box % 3 == 1:
                col_range = [3, 4, 5]
            else:
                col_range = [6,7,8]
            if box <= 2:
                row_range = [0, 1, 2]
            elif box <= 5:
                row_range = [3, 4, 5]
            else:
                row_range = [6, 7, 8]
            
            for i in row_range:
                for j in col_range:
                    num = None if board[i][j] == "." else int(board[i][j])
                    if not num:
                        continue
                    if p[num]:
                        return False
                    p[num] = True
            return True
        for i in range(9):
            if not (checkRow(i) and checkCol(i) and checkBox(i)):
                return False
        return True