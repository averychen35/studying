class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n # bottom row is all 1 since you can only go right

        for i in range(m-1):
            newRow = [1] * n # the rightmost col is always default 1
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + row[j] # add the bottom and right
            row = newRow
        return row[0]
        