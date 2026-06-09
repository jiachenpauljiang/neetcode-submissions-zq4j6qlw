class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        This is asking for the shortest distance between 2 islands
        1. DFS to find the first island 
        2. BFS to find the shortest distance 
        """
        first = None

        N = len(grid)

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    first = (r, c)
                    break
            if first:
                break
        
        # queue to hold the first islands 
        queue = deque()
        def dfs(r, c):
            # mark as visited
            grid[r][c] = 2

            # 0 means distance to the first island is 0
            queue.append((r, c, 0))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 1:
                    dfs(nr, nc)
        
        dfs(*first)

        while queue:
            r, c, dist = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                
                if grid[nr][nc] == 1:
                    return dist
                
                if grid[nr][nc] == 2:
                    continue
                
                grid[nr][nc] = 2
                queue.append((nr, nc, dist + 1))