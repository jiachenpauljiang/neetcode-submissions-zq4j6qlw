class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Find all the treasure cells 
        BFS to expand, for each land cell met, replace value with distance 
        """

        queue = deque()

        R, C = len(grid), len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    # 0 means the distance to the nearest treasure 
                    queue.append((i, j, 1))
        
        while queue:
            r, c, dist = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < R and 0 <= nc < C):
                    continue
                if grid[nr][nc] != 2147483647:
                    continue
                grid[nr][nc] = dist
                queue.append((nr, nc, dist + 1))
                