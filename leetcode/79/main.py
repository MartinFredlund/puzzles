from collections import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if self.dfs(board, r, c, word, 0):
                        return True
        return False

    def dfs(self, board, r, c, word, index):
        if board[r][c] != word[index]:
            return False
        elif board[r][c] == word[index] and index == len(word) - 1:
            return True
        temp = board[r][c]
        board[r][c] = "#"

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                if self.dfs(board, nr, nc, word, index + 1):
                    return True

        board[r][c] = temp
        return False
