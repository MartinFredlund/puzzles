from typing import List
from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        parent = [i for i in range(n + 1)]
        result = []

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        for u, v in edges:
            u_parent = find(u)
            v_parent = find(v)
            if u_parent == v_parent:
                result.append([u, v])
            else:
                parent[u_parent] = v_parent
        return result[-1]


s = Solution()
print(s.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5], [2, 4]]))
