class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(r, c):
            # base case 
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or (r, c) in visited or grid[r][c] == 0:
                return 0
            visited.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1)
        
        area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = max(area, dfs(i, j))
        return area 