class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_count = 0
        rotten_queue = deque()

        ROWS, COLS = len(grid), len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    rotten_queue.append((i, j))
        
        minute = 0
        while rotten_queue and fresh_count > 0:
            minute += 1
            for _ in range(len(rotten_queue)):
                cur_r, cur_c = rotten_queue.popleft()

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for d_r, d_c in directions:
                    n_r, n_c = cur_r + d_r, d_c + cur_c
                    if 0 <= n_r < ROWS and 0 <= n_c < COLS and grid[n_r][n_c] == 1:
                        grid[n_r][n_c] = 2
                        fresh_count -= 1
                        rotten_queue.append((n_r, n_c))
        
        return minute if fresh_count == 0 else -1