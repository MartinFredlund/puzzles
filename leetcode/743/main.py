from typing import List
from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacent_list = defaultdict(list)
        for s, v, w in times:
            adjacent_list[s].append((v, w))
        min_heap = [(0, k)]
        visited = set()
        max_time = 0
        while min_heap:
            time, node = heapq.heappop(min_heap)

            if node in visited:
                continue
            else:
                visited.add(node)
            max_time = time
            for v, w in adjacent_list[node]:
                heapq.heappush(min_heap, (time + w, v))
        return max_time if len(visited) == n else -1
