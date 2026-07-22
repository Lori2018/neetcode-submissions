class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        horizontal_maps = []
        vertical_maps = []
        box_maps = []
        for i in range(9):
            horizontal_maps.append(set())
            vertical_maps.append(set())
            box_maps.append(set())

        # iterate through board
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                num = int(board[i][j])
                box_num = (i // 3) * 3 + (j // 3)
                if num in horizontal_maps[i]:
                    return False 
                elif num in vertical_maps[j]:
                    return False 
                elif num in box_maps[box_num]:
                    return False 
                horizontal_maps[i].add(num)
                vertical_maps[j].add(num)
                box_maps[box_num].add(num)
        return True

    
