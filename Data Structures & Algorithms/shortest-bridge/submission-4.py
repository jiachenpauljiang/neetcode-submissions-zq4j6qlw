class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        This is really asking about the minimum distance between the two island 

        First use DFS to find all the cells in island one 

        Then, use BFS to find the minimum distance between the first and second island 
        """

        n = len(grid)

        # represents the first cell we find for island one 
        first_cell = None 

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # find any cell with value 1 
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    first_cell = (r, c)
                    break
            if first_cell:
                break 
        
        queue = deque()
        # DFS to find all islands 
        def dfs(r, c):
            # add island one cell to the queue with distance 0
            queue.append((r, c, 0)) 
            # mark the cell as visited 
            grid[r][c] = 2

            for dr, dc in directions:
                nr, nc = r + dr, c + dc 

                # check nr, nc validity 
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    # another valid cell
                    dfs(nr, nc)
        
        dfs(*first_cell)

        # now BFS the queue with all the first island cells
        while queue:
            r, c, dist = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < n and 0 <= nc < n):
                    continue 
                
                if grid[nr][nc] == 2:
                    continue 
                
                if grid[nr][nc] == 1:
                    return dist 
                
                grid[nr][nc] = 2
                queue.append((nr, nc, dist + 1))
        
        return -1 