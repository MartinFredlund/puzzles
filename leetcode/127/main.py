from typing import List
from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        neighbor_words = defaultdict(list)
        queue = deque()
        wordList.append(beginWord)
        for w in wordList:
            for i in range(len(w)):
                pattern = w[:i] + "*" + w[i + 1 :]
                neighbor_words[pattern].append(w)

        visited = set()
        queue.append(beginWord)
        visited.add(beginWord)
        num_of_words = 1
        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                word = queue.popleft()
                if word == endWord:
                    return num_of_words
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1 :]
                    for next_word in neighbor_words[pattern]:
                        if next_word not in visited:
                            visited.add(next_word)
                            queue.append(next_word)
            num_of_words += 1

        return 0


s = Solution()

print(
    s.ladderLength(
        beginWord="hit",
        endWord="cog",
        wordList=["hot", "dot", "dog", "lot", "log", "cog"],
    )
)
