class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        Asking the minimum distance between 2 island

        Use DFS to find all cells of the first island 

        Use BFS to expand from all cells of the first island, until reaching the second island for the first time 
        """

        N = len(grid)

        first = None 

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    first = (r, c)
                    break
            if first:
                break
        
        # queue to hold cells of the first island
        queue = deque()
        def dfs(r, c):
            # mark cell as visited
            grid[r][c] = 2
            queue.append((r, c, 0)) # the 3rd element is the distance towards the first island 

            for dr, dc in directions:
                nr, nc  = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 1:
                    dfs(nr, nc)
        dfs(*first)

        # now the queue should hold all cells of the first island. 
        # In the grid, the first island cells are marked as 2

        while queue:
            r, c, dist = queue.popleft()
            for dr, dc in directions:
                nr, nc  = r + dr, c + dc

                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if grid[nr][nc] == 2:
                    continue
                if grid[nr][nc] == 1:
                    return dist
                
                grid[nr][nc] = 2
                queue.append((nr, nc, dist + 1))
        return -1