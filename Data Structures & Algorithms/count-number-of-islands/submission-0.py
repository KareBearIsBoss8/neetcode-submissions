class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def helper(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == "0":
                return
            
            grid[row][col] = '0'
            for i, j in directions:
                helper(row + i, col + j)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    helper(r, c)
                    islands += 1
        return islands
