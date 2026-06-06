class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        This is asking the minimum distance between two islands
        First use DFS to find the first island 
        Then BFS to find the distance to the first 1 we see 
        """
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        first = None
        for r in range(len(grid)):
            for c in range(len(grid)):
                if grid[r][c] == 1:
                    first = (r, c)
                    break
            if first:
                break
        
        # queue to store the first islands to begin BFS next step
        queue = deque()
        def dfs(r, c):
            # mark cell as visited
            grid[r][c] = 2

            # note the distance to the first island - here it's 0
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
                    # out of bounds 
                    continue 
                
                if grid[nr][nc] == 2:
                    # visited 
                    continue 

                if grid[nr][nc] == 1:
                    # we reached the first cell of the second island 
                    return dist 
                
                # if not, continue searching 
                grid[nr][nc] = 2
                queue.append((nr, nc, dist + 1))