from collections import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            if board[i][0] == "0":
                self.find_segment(board, i, 0)
            if board[i][len(board[0]) - 1] == "0":
                self.find_segment(board, i, len(board[0]) - 1)
            if board[0][i] == "0":
                self.find_segment(board, 0, i)
            if board[len(board) - 1][i] == "0":
                self.find_segment(board, len(board) - 1, i)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "0":
                    board[r][c] = "X"
                if board[r][c] == "t":
                    board[r][c] = "0"

    def find_segment(self, board, r, c):

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        if board[r][c] == "0":
            board[r][c] = "t"
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                    self.find_segment(board, nr, nc)
