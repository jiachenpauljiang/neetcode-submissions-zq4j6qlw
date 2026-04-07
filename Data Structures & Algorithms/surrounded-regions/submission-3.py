class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            # searching for the "O" and turn them into "X" for the "O"s connected to the border 
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != "O":
                return
            board[r][c] = "T"

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in directions:
                n_r, n_c = r + dr, c + dc
                dfs(n_r, n_c)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O" and (i in [0, ROWS - 1] or j in [0, COLS - 1]):
                    dfs(i, j)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"