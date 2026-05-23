class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        Find the first island 
        DFS to find all cells of the first island 
        BFS to find the closest path to the second island 
        """
        
        first = None
        n = len(grid)
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    first = (r, c)
                    break
                
            if first:
                break
        
        queue = deque()
        # DFS to find all the cells of the first island, mark them as 2
        def dfs(r, c):
            grid[r][c] = 2 # mark as visited
            queue.append((r, c, 0))
            for dr, dc, in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    dfs(nr, nc)
        
        dfs(*first)

        # BFS to expand from the first island 
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
                
                if grid[nr][nc] == 0:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, dist + 1))
        return -1