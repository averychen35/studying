class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # go through values, and if we find an island do dfs
        # keep a counter of how many times dfs has to be called
        # during dfs, set all values equal to 0 including starting value
        # while curr = 1 continue
        counter = 0

        def dfs(row, col):
            adj = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            if grid[row][col] == "1":
                grid[row][col] = 0
                for val in adj:
                    new_row = row + val[0]
                    new_col = col + val[1]
                    if new_row >= 0 and new_row < len(grid) and new_col >= 0 and new_col < len(grid[0]):
                        dfs(new_row, new_col)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    
                    dfs(i, j)
                    counter += 1
        
        return counter
        



        