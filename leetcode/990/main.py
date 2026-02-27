from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}

        def find(index):
            if index not in parent:
                parent[index] = index

            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]

        for x, op, _, y in equations:
            if op == "=":
                parent[find(x)] = find(y)

        for x, op, _, y in equations:
            if op == "!":
                if find(x) == find(y):
                    return False

        return True


s = Solution()
print(s.equationsPossible(equations=["a==b", "b!=a"]))
