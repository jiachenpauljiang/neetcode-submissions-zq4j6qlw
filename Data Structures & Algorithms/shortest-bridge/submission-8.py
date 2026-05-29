class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        1. Use DFS to find all cells of the first island 
        2. Use BFS to determine the minimum distance to the second island
        """

        N = len(grid)
        first = None # record the first 1 cell of the first island 
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    first = (r, c)
                    break 
            if first:
                break 
        
        queue = deque() # queue storing all the cells of the first island 
        def dfs(r, c):
            queue.append((r, c, 0))
            grid[r][c] = 2 # mark as visited 

            for dr, dc in directions:
                nr, nc = r + dr, c + dc 

                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 1:
                    dfs(nr, nc)
        dfs(*first)

        # at this point, we have found our first island, modified the cell values to 2, and stored the (r, c) in queue 

        while queue:
            r, c, dist = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < N and 0 <= nc < N):
                    # out of bounds 
                    continue 
                
                if grid[nr][nc] == 2:
                    # visited 
                    continue 
                
                if grid[nr][nc] == 1:
                    # found the second island 
                    return dist 

                grid[nr][nc] = 2
                queue.append((nr, nc, dist + 1))
        return -1 