class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0 or (r,c) in visited:
                return 0
            visited.add((r,c))

            return 1 + dfs(r+1, c) + dfs(r-1,c) + dfs(r, c+1) + dfs(r, c-1)
        
        area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                area = max(area, dfs(r, c))
        return area 