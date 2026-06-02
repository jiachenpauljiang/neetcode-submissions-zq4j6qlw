class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        first = None 
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    first = (r, c)
                    break 
            if first:
                break 
        
        queue = deque() # store the first island cells 
        # find the first island 
        def dfs(r, c):
            grid[r][c] = 2 # mark as visited 
            queue.append((r, c, 0)) # 0 here is the distance to the first island 

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 1:
                    dfs(nr, nc)
        dfs(*first)

        # BFS to find the minimum distance between the first and second island 
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
        