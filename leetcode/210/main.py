from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        cycle = set()
        visiting = set()
        result = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visiting:
                return True

            cycle.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            cycle.remove(crs)

            visiting.add(crs)
            result.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return result
