class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        This is asking the minimum distance between the 2 islands
        1. DFS to find all cells for the first island 
        2. BFS to find the distance to any cell of the second island
        """
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        N = len(grid)
        first = None
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    first = (r, c)
                    break
            if first:
                break
        
        # queue to store the cells of the first island
        queue = deque()

        def dfs(r, c):
            # mark as visited
            grid[r][c] = 2

            # 0 means distance to the first island
            queue.append((r, c, 0))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 1:
                    dfs(nr, nc)
        dfs(*first)

        # Now we have a queue with all the island one cells, and all island one cells in grid has been changed to 2

        while queue:
            r, c, dist = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if grid[nr][nc] == 2:
                    continue
                if grid[nr][nc] == 1:
                    return dist
                
                queue.append((nr, nc, dist + 1))
                grid[nr][nc] = 2