class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def helper(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0
            curr = 1
            for i, j in directions:
                curr += helper(row + i, col + j)
            return curr

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    curr = helper(r, c)
                    islands = max(islands, curr)
        return islands
