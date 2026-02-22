from collections import List, deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue = deque()
        for r in range(len(grid)):
            for c in range(len(grid)):
                if grid[r][c] == 1:
                    queue.append((r, c))

        if len(queue) in {len(grid) * len(grid), 0}:
            return -1
        largest_dist = -1
        while queue:
            r, c = queue.popleft()

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid) and grid[nr][nc] == 0:
                    grid[nr][nc] = grid[r][c] + 1
                    largest_dist = max(grid[nr][nc] - 1, largest_dist)
                    queue.append((nr, nc))
        return largest_dist
