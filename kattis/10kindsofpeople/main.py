import sys


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1


def get_labyrinth_from_cmd():
    lines = sys.stdin.read().splitlines()
    iterator = iter(lines)
    row, col = map(int, next(iterator).split())

    labyrinth = []
    for _ in range(row):
        labyrinth.append(list(next(iterator).strip()))

    n = int(next(iterator))

    points = []
    for _ in range(n):
        a, b, c, d = map(int, next(iterator).split())
        points.append(((a - 1, b - 1), (c - 1, d - 1)))

    return labyrinth, points, row, col


if __name__ == "__main__":
    maze, points, rows, cols = get_labyrinth_from_cmd()

    # Build Union-Find structure
    uf = UnionFind(rows * cols)

    for r in range(rows):
        for c in range(cols):
            idx = r * cols + c
            if c + 1 < cols and maze[r][c] == maze[r][c + 1]:
                uf.union(idx, idx + 1)
            if r + 1 < rows and maze[r][c] == maze[r + 1][c]:
                uf.union(idx, idx + cols)

    for p in points:
        r1, c1 = p[0]
        r2, c2 = p[1]
        idx1 = r1 * cols + c1
        idx2 = r2 * cols + c2

        if uf.find(idx1) == uf.find(idx2):
            if maze[r1][c1] == "0":
                print("binary")
            else:
                print("decimal")
        else:
            print("neither")
