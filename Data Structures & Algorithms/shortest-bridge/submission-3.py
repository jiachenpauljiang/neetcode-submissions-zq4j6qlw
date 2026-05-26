class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        First use DFS to find the first island
        Then use BFS to find the miniimum path to the second island 
        """

        n = len(grid)
        first = None
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    # found one of the cells of the first island 
                    first = (r, c)
                    break

            if first:
                break
        
        # dfs to find all cells of the first island and store them in a queue 
        queue = deque()

        def dfs(r, c):
            # mark as visited 
            grid[r][c] = 2

            # append to queue with distance 0
            queue.append((r, c, 0))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    dfs(nr, nc)
        dfs(*first)

        # now we have a queue of all the first island cells 

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
                    # found it 
                    return dist 
                
                # otherwise continue searching 
                grid[nr][nc] = 2
                queue.append((nr, nc, dist + 1))

        return -1 