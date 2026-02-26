from typing import List
from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque()
        grid_len = len(grid)
        if not (grid[0][0] == 0 and grid[grid_len - 1][grid_len - 1] == 0):
            return -1

        queue.append((0, 0))
        depth = 0
        directions = [
            (1, 0),
            (1, 1),
            (-1, 0),
            (-1, 1),
            (0, 1),
            (0, -1),
            (1, -1),
            (-1, -1),
        ]
        while queue:
            level_size = len(queue)
            depth += 1
            for _ in range(level_size):
                r, c = queue.popleft()
                if r == grid_len - 1 and c == grid_len - 1:
                    return depth

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < grid_len and 0 <= nc < grid_len and grid[nr][nc] == 0:
                        grid[nr][nc] = depth
                        queue.append((nr, nc))
        return -1


s = Solution()
print(s.shortestPathBinaryMatrix(grid=[[1, 0, 0], [1, 1, 0], [1, 1, 0]]))
