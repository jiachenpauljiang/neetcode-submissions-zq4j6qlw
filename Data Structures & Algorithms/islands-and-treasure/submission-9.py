class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Logic

        Expand from each treasure cell, noting the current distance from the cell.
        If encountering a INF cell, update the value to the current distance 
        """
        
        INF = 2147483647

        # queue to hold the initial treasure islands 
        queue = deque()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r, c))

        dist = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == INF:
                        grid[nr][nc] = dist
                        queue.append((nr, nc))
            dist += 1