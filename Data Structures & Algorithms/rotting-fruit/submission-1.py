class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        fresh = 0
        time = 0

        fruits = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    fruits.append((r,c))
        
        while fresh > 0 and fruits:
            for i in range(len(fruits)):
                (r, c) = fruits.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if (row in range(rows) and col in range(cols) and grid[row][col] == 1):
                        grid[row][col] = 2
                        fruits.append((row, col))
                        fresh -= 1
            time += 1
        
        if fresh == 0:
            return time
        return -1
