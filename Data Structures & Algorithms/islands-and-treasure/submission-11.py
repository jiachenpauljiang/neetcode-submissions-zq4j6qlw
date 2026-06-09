class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        1. Find all the treasure cells 
        2. From each treasure cell, BFS to find all INF cells, taking note of the current distance 
        """

        R, C = len(grid), len(grid[0])

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        queue = deque() # hold the treasure islands 
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
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 2147483647:
                        grid[nr][nc] = dist
                        queue.append((nr, nc))
            dist += 1