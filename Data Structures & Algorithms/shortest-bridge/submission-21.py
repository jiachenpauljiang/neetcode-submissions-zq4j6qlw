class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        This is really asking the shortest distance between
        two islands 
        """

        # First, find all cells belonging to island one 
        First = None
        N = len(grid)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    First = (r, c)
                    break
            if First:
                break
        
        # Found the first cell, now DFS to find the rest 
        queue = deque()
        def dfs(r, c):
            # mark grid as visited
            grid[r][c] = 2
            # 0 means distance to the first island 
            queue.append((r, c, 0))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 1:
                    dfs(nr, nc)
        dfs(*First)

        # now BFS to find the shortest distance to the second island 
        while queue:
            r, c, dist = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if grid[nr][nc] == 1:
                    return dist
                if grid[nr][nc] == 2:
                    continue
                queue.append((nr, nc, dist + 1))
                grid[nr][nc] = 2