import math
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # rows need to become cols, and vice versa
        # at any given time, need to store 1 row and 1 col
        # xor: if you a ^ b ^ b = a
        # formula: 
        # (0, 0) -> (0, n-1)
        # (0, 1) -> (1, n-1)
        # (1, 0) -> (0, 1 aka n-2)

        # (i, j) -> (j, n-i-1)
        n = len(matrix)

        def clockwise(tup):
            i, j = tup
            return (j, n-i-1)

        def replace(i, j):
            i1, j1 = clockwise((i, j))
            i2, j2 = clockwise((i1, j1))
            i3, j3 = clockwise((i2, j2))

            temp = matrix[i1][j1]
            matrix[i1][j1] = matrix[i][j]
            temp1 = matrix[i2][j2]
            matrix[i2][j2] = temp
            temp = matrix[i3][j3]
            matrix[i3][j3] = temp1
            matrix[i][j] = temp
        for i in range(math.ceil(n/2)):
            for j in range(i, n-i-1):
                replace(i, j)

# [13,9,3,1],
# [5,10,6,2],
# [15,11,7,12],
# [16,14,8,4]

# [13,9,5,1],
# [14,10,6,2],
# [15,11,7,3],
# [16,12,8,4]