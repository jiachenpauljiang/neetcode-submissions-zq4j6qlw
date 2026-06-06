class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])
        INF = 2147483647
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        """
        Start from each treasure cell, expand step by step, and
        turn the land cells encountered into step count 
        """

        # queue that holds initial treasure cells 
        queue = deque()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    queue.append((r, c))

        dist = 1

        while queue:
            cur_cell_count = len(queue)
            
            for _ in range(cur_cell_count):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == INF:
                        grid[nr][nc] = dist
                        queue.append((nr, nc))
            dist += 1