class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # use a set to keep track of currently visited
        visited=set()
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(row, col, count):
            if (row < 0 or col < 0 or row >= ROWS or col >= COLS or board[row][col] != word[count] or (row, col) in visited):
                return False
            elif count == len(word) -1:
                return True
            else:
                visited.add((row, col))
                res = (dfs(row + 1, col, count + 1) or 
                dfs(row - 1, col, count + 1) or 
                dfs(row, col + 1, count + 1) or 
                dfs(row, col - 1, count + 1))
                visited.remove((row, col))
                return res
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
            


        