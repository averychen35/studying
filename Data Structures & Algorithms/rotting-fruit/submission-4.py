class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while fresh > 0 and q: # more things to rot and more reachable things to rot
            to_rot = len(q)
            for _ in range(to_rot):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row in range(len(grid)) and col in range(len(grid[0])):
                        if grid[row][col] == 1:
                            q.append((row, col))
                            grid[row][col] = 2 # we want to rot this orange after adding it
                            fresh -= 1
            time += 1
        return time if fresh == 0 else -1 # if not possible to rot everything
                    


        