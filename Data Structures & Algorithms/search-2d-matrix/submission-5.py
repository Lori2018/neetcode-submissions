class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search rows
        # search rows
        loRow = 0
        hiRow = len(matrix) - 1
        row = (hiRow - loRow) // 2

        while loRow <= hiRow: 
            if target < matrix[loRow][0] or target > matrix[hiRow][len(matrix[0]) - 1]:
                return False
            if target >= matrix[row][0] and target <= matrix[row][len(matrix[0]) - 1]:
                loCol = 0 
                hiCol = len(matrix[0]) - 1 
                col = (hiCol - loCol) // 2 + loCol
                while loCol <= hiCol: 
                    if target < matrix[row][loCol] or target > matrix[row][hiCol]:
                        return False
                    if target == matrix[row][col]:
                        return True 
                    elif target < matrix[row][col]:
                        hiCol = col - 1
                    else: 
                        loCol = col + 1
                    col = (hiCol - loCol) // 2 + loCol
                return False
            elif target < matrix[row][0]:
                hiRow = row - 1
            else: 
                loRow = row + 1
            row = (hiRow - loRow) // 2 + loRow 
        return True if target == matrix[row][0] else False

