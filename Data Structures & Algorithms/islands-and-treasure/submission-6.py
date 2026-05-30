class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Find all the `0` cells, add into a queue 
        Expand outwards, and mark INF cells as the distance, add these INF cells to the queue 
        """
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        INF = 2147483647

        M, N = len(grid), len(grid[0])

        queue = deque()

        for m in range(M):
            for n in range(N):
                if grid[m][n] == 0:
                    queue.append((m, n))
        
        dist = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < M and 0 <= nc < N and grid[nr][nc] == INF:
                        grid[nr][nc] = dist
                        queue.append((nr, nc))
            dist += 1