from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0 for _ in range(len(rooms))]

        def findKeys(index):
            for key in rooms[index]:
                if visited[key] == 0:
                    visited[key] = 1
                    findKeys(key)

        visited[0] = 1

        findKeys(0)
        return all(found == 1 for found in visited)


s = Solution()
print(s.canVisitAllRooms(rooms=[[1, 3], [3, 0, 1], [2], [0]]))
