from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(r, c):
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
                if (r, c) in visited:
                    return 0
                visited.add((r, c))
                return dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

            else:
                return 1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return dfs(
                        r,
                        c,
                    )


s = Solution()
print(s.islandPerimeter(grid=[[1, 0]]))
