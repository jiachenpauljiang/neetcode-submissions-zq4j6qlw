class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        Asking the minimum distance between two islands 

        DFS to find all cells of the first island 

        BFS from all cells of the first island to the first reachable cell of the second island 
        """

        N = len(grid)
        first = None 
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    first = (r, c)
        
        queue = deque()
        def dfs(r, c):
            # mark as visited 
            grid[r][c] = 2

            queue.append((r, c, 0))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc 

                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 1:
                    dfs(nr, nc)
        dfs(*first)

        # All the cells of the first island are marked as 2 now and added to queue 

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
        
        return -1