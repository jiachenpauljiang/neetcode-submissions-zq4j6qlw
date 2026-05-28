class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        First use DFS to find all cells belonging to the first island 
        Then use BFS to find the shortest distance between the first island and any cells of the second island
        """

        n = len(grid)
        first = None 
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # try to find the first island 
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    first = (r, c)
                    break
            if first:
                break 
        
        queue = deque()
        def dfs(r, c):
            # mark the cell as visited
            grid[r][c] = 2
            queue.append((r, c, 0)) # 0 is distance to the first island 

            for dr, dc in directions:
                nr, nc = r + dr, c + dc 

                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    dfs(nr, nc)
        
        dfs(*first)

        # now BFS to find the shortest path 
        while queue:
            r, c, dist = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc 

                if not (0 <= nr < n and 0 <= nc < n):
                    # out of bounds 
                    continue 
                
                if grid[nr][nc] == 2:
                    # visited 
                    continue 
                
                if grid[nr][nc] == 1:
                    return dist
                
                # mark visited 
                grid[nr][nc] = 2
                queue.append((nr, nc, dist + 1))

        return -1