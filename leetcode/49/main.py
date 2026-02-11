from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if strs == None or len(strs) == 0:
            return []
        groups = defaultdict(list)

        for s in strs:
            count = [0 for _ in range(26)]
            for c in s:
                count[ord(c) - ord("a")] += 1
            key = tuple(count)
            groups[key].append(s)

        return list(groups.values())


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
