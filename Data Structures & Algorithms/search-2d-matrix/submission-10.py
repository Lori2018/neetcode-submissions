class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find row number
        i = 0
        j = len(matrix)
        while i < j:
            mid = (i+j)//2
            if target == matrix[mid][0]:
                return True
            elif target < matrix[mid][0]:
                j = mid-1
            else:
                i = mid+1
        i = min(min(i, j), len(matrix)-1)
        x = 0
        y = len(matrix[0])
        while x < y:
            mid = (x+y)//2
            if target == matrix[i][mid]:
                return True
            elif target < matrix[i][mid]:
                y = mid-1
            else:
                x = mid+1
        x = min(x, len(matrix[0])-1)
        return target == matrix[i][x] 