from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        visited_pacific = set()
        visited_atlantic = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, ocean):
            if (r, c) in ocean:
                return
            ocean.add((r, c))
            for dr, dc in directions:
                nr, nc = dr + r, dc + c

                if (
                    0 <= nr < len(heights)
                    and 0 <= nc < len(heights[0])
                    and heights[r][c] <= heights[nr][nc]
                ):
                    dfs(nr, nc, ocean)

        for i in range(len(heights)):
            dfs(i, 0, visited_pacific)
            dfs(i, len(heights[0]) - 1, visited_atlantic)
        for i in range(len(heights[0])):
            dfs(0, i, visited_pacific)
            dfs(len(heights) - 1, i, visited_atlantic)

        res = visited_atlantic.intersection(visited_pacific)
        return [list(coord) for coord in res]


s = Solution()
print(
    s.pacificAtlantic(
        heights=[
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
    )
)
