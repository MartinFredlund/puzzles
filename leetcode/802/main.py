from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        safe_node = []
        safe_map = {}

        def dfs(index):
            if index in safe_map:
                return safe_map[index]

            safe_map[index] = False

            for i in graph[index]:
                if not dfs(i):
                    return False
            safe_map[index] = True

            return True

        for i in range(len(graph)):
            if dfs(i):
                safe_node.append(i)
        return safe_node


s = Solution()
print(s.eventualSafeNodes(graph=[[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]))
