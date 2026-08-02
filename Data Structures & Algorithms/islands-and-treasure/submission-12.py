class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # run bfs from each treasure chest simultaneously
        # ensure we only have to set each value once
        queue = deque()
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])

        def addRoom(row, col):
            if row < 0 or row >= ROWS or col < 0 or col >=COLS or grid[row][col] < 0 or (row, col) in visited:
                return
            visited.add((row, col))
            queue.append([row, col])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append([r, c])
                    visited.add((r, c))
        
        dist = 0

        while queue:
            for i in range(len(queue)):
                r, c, = queue.popleft()
                grid[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c-1)
            dist += 1
                    


        
        