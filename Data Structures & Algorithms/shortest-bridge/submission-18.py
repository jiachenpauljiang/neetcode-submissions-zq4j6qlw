class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        This is really asking the shortest distance between two islands 
        """

        # First, find the first island 
        first = None
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 1:
                    first = (i, j)
                    break
            if first:
                break
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = deque()
        
        def dfs(r, c):
            # mark as visited
            grid[r][c] = 2
            # 
            queue.append((r, c, 0))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < len(grid) and 0 <= nc < len(grid) and grid[nr][nc] == 1:
                    dfs(nr, nc)
        dfs(*first)

        while queue:
            r, c, dist = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < len(grid) and 0 <= nc < len(grid)):
                    continue
                
                if grid[nr][nc] == 2:
                    continue
                
                if grid[nr][nc] == 1:
                    return dist
                
                queue.append((nr, nc, dist + 1))
                grid[nr][nc] = 2