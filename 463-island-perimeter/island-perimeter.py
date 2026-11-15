class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 1
                    if i < rows - 1 and grid[i + 1][j] == 1:
                        perimeter -= 1
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 1
                    if j < cols - 1 and grid[i][j + 1] == 1:
                        perimeter -= 1

        return perimeter
