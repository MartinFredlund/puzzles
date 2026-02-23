from typing import List
from collections import defaultdict


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        city_connection = defaultdict(list)
        for r in range(len(isConnected)):
            for c in range(len(isConnected)):
                if isConnected[r][c]:
                    city_connection[r + 1].append(c + 1)
        visited = set()

        def dfs(node):
            visited.add(node)
            for v in city_connection[node]:
                if v not in visited:
                    dfs(v)

        amount_provinces = 0

        for k in city_connection.keys():
            if not k in visited:
                amount_provinces += 1
                dfs(k)
        return amount_provinces
