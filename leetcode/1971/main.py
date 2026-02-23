from typing import List
from collections import defaultdict


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        adjacency_list = defaultdict(list)
        for s, d in edges:
            adjacency_list[s].append(d)
            adjacency_list[d].append(s)

        visited = set()

        def dfs(node):
            if node == destination:
                return True
            if node in visited:
                return False
            visited.add(node)

            for v in adjacency_list[node]:
                if dfs(v):
                    return True
            return False

        return dfs(source)


s = Solution()
print(
    s.validPath(
        n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source=0, destination=5
    )
)
