class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        We can instead expand on known treasure islands and change the land cells encountered along the way 
        """
        INF = 2147483647

        queue = deque() # hold treasure cells 

        R, C = len(grid), len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

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
                        grid[nr][nc] = dist
                        queue.append((nr, nc))
            dist += 1