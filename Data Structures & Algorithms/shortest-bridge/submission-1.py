class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        Logic: 

        First use DFS to identify all cells belong to the first island. Mark all cells as "visited", for example marking them as 2

        Then, use BFS to search for the second island. 
        """

        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        first = None

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    # found the first island, note the coordinate 
                    first = (r, c)
                    break
            if first:
                break

        queue = deque()
        def dfs(r, c):
            grid[r][c] = 2 # mark as visited
            queue.append((r, c, 0)) 
            # DFS to find all cells of the first island
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    # store the coordinate and the distance to the first island
                    dfs(nr, nc)
        dfs(*first)

        # now queue should contain a bunch of (r, c, 0) points
        while queue:
            r, c, distance = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < n and 0 <= nc < n):
                    # out of bounds
                    continue 
                if grid[nr][nc] == 2:
                    # visited in island one
                    continue
                if grid[nr][nc] == 1:
                    # we found it! 
                    return distance
                grid[nr][nc] = 2
                queue.append((nr, nc, distance + 1))
        return -1