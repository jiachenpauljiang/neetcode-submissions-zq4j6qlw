class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if r < 0 or r < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r, c + 1)
            capture(r - 1, c)
            capture(r, c - 1)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O" and i in [0, ROWS - 1] or j in [0, COLS - 1]:
                    capture(i, j)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O": 
                    board[i][j] = "X"

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "T": 
                    board[i][j] = "O"
