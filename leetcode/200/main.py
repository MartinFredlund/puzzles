from types import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    island_count += 1
                    self.removeIsland(grid, r, c)
        return island_count

    def removeIsland(self, grid, r, c):
        if r < 0 or c < 0 or len(grid) <= r or len(grid[0]) <= c:
            return
        if grid[r][c] == "1":
            grid[r][c] = "0"
            self.removeIsland(grid, r + 1, c)
            self.removeIsland(grid, r - 1, c)
            self.removeIsland(grid, r, c + 1)
            self.removeIsland(grid, r, c - 1)
