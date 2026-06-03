class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        """
        DFS to find the first island
        BFS to find the minimum distance
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

        # so far we found the first (r, c) of the first island, now DFS to find all connected islands

        queue = deque()  # to hold island 1 cells

        def dfs(r, c):
            # mark as visited
            grid[r][c] = 2
            queue.append((r, c, 0))  # 0 is the distance to the first island

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
                grid[nr][nc] = 2
                queue.append((nr, nc, dist + 1))
