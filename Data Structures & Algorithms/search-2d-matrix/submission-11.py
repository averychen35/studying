class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find correct row
        # check if value exists in that row
        ROWS, COLS = len(matrix) - 1, len(matrix[0]) - 1
        row = 0
        top, bot = 0, ROWS
        while top <= bot:
            row = (top + bot) // 2
            if target < matrix[row][0] and target <= matrix[row][-1]:
                bot = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break # this row is good
        
        if not (top <= bot):
            return False
        
        l, r = 0, COLS
        while l <= r:
            col = (l + r) // 2
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                r = col - 1
            else:
                l = col + 1
        return False

        