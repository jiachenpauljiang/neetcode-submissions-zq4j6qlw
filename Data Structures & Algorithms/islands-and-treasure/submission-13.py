class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Collect all the treasure cells 
        Expand outwards step by step. At each step, if encountering a land cell, change the land cell to the step count 
        """

        R, C = len(grid), len(grid[0])

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        # queue to hold initial treasure cells 
        queue = deque()

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