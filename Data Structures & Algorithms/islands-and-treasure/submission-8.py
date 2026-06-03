class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Instead of filling each land cell with the distance to the nearest treasure cell,
        we can expand upon each treasure cell step by step, and fill the land cells encountered 
        with the current distance 
        """

        R, C = len(grid), len(grid[0])

        queue = deque() 

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        INF = 2147483647

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        dist = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == INF:
                        queue.append((nr, nc))
                        grid[nr][nc] = dist
            dist += 1