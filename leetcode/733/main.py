from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        start_color = image[sr][sc]

        def flip_color(r, c):
            if (
                0 <= r < len(image)
                and 0 <= c < len(image[0])
                and image[r][c] == start_color
            ):

                image[r][c] = color
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    flip_color(nr, nc)

        flip_color(sr, sc)
        return image


s = Solution()
print(s.floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, color=2))
