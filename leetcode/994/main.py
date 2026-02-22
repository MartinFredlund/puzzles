from collections import deque


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        queue = deque()
        fresh_count = 0
        minutes = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue and fresh_count > 0:
            level_size = len(queue)

            for _ in range(level_size):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < len(grid)
                        and 0 <= nc < len(grid[0])
                        and grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))

            minutes += 1

        if fresh_count > 0:
            return -1
        return minutes


solve = Solution()
print(solve.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
