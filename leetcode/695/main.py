from types import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_size = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    temp = self.removeIsland(grid, r, c)
                    island_size = max(temp, island_size)
        return island_size

    def removeIsland(self, grid, r, c):
        current_size = 0
        if r < 0 or c < 0 or len(grid) <= r or len(grid[0]) <= c:
            return current_size
        if grid[r][c] == 1:
            grid[r][c] = 0
            current_size += (
                1
                + self.removeIsland(grid, r + 1, c)
                + self.removeIsland(grid, r - 1, c)
                + self.removeIsland(grid, r, c + 1)
                + self.removeIsland(grid, r, c - 1)
            )
        return current_size
