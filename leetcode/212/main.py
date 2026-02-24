from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word
        R, C = len(board), len(board[0])

        res, visited = set(), set()

        def dfs(r, c, node):
            if (
                r < 0
                or c < 0
                or r >= R
                or c >= C
                or (r, c) in visited
                or board[r][c] not in node.children
            ):
                return

            child_node = node.children[board[r][c]]

            if child_node.word is not None:
                res.add(child_node.word)

            visited.add((r, c))

            dfs(r + 1, c, child_node)
            dfs(r - 1, c, child_node)
            dfs(r, c + 1, child_node)
            dfs(r, c - 1, child_node)
            visited.remove((r, c))

        for r in range(R):
            for c in range(C):
                dfs(r, c, root)
        return list(res)
