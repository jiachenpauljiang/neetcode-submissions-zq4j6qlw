class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        This is asking the min distance between 2 islands

        First, do a DFS to identify all the cells of the first island. Change the cell value
        to 2 to mark them as visited.

        Then, do a BFS from the first island the find the minimum distance to the second island
        """

        # Finding the first island
        n = len(grid)
        first = None # will be replaced with (r, c) of the first cell that is 1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

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
            # enqueue the cell with the distance to the first island
            queue.append((r, c, 0)) 

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                    dfs(nr, nc)
        
        dfs(*first)

        # BFS to find the second island 
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