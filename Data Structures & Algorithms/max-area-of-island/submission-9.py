class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visit = set()

        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0 or (row, col) in visit:
                return 0
            visit.add((row, col))
            return 1 + dfs(row -1, col) + dfs(row + 1, col) + dfs(row, col + 1) + dfs(row, col-1)
            
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = max(area, dfs(i, j))
        
        return area
        