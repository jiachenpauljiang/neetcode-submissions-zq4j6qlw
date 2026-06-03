class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        1. Find the first island 
            1.1 Find any cell with value 1
            1.2 DFS to find all connected cells 
        2. BFS to find the minimum distance to the second island 
        """
        first = None 

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(len(grid)):
            for c in range(len(grid)):
                if grid[r][c] == 1:
                    first = (r, c)
                    break
            if first:
                break
        
        queue = deque()
        def dfs(r, c):
            # mark as visited 
            grid[r][c] = 2

            # store in the queue, 0 means distance 0 to the first island (itself)
            queue.append((r, c, 0))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid) and grid[nr][nc] == 1:
                    dfs(nr, nc)
        dfs(*first)

        # now we have marked all island 1 cell as visited
        # and we have queued up all island 1 cells 

        while queue:
            r, c, dist = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < len(grid) and 0 <= nc < len(grid) and grid[nr][nc] != 2:
                    if grid[nr][nc] == 1:
                        return dist 
                
                    queue.append((nr, nc, dist + 1))
                    grid[nr][nc] = 2