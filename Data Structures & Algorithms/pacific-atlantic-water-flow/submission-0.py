class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pacificSet = set()
        atlanticSet = set()
        res = []

        def dfs(r, c, visited, prevHeight):
            if (r, c) in visited or r < 0 or r >= ROWS or c < 0 or c >= COLS or heights[r][c] < prevHeight:
                return
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pacificSet, heights[0][c])
            dfs(ROWS - 1, c, atlanticSet, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pacificSet, heights[r][0])
            dfs(r, COLS - 1, atlanticSet, heights[r][COLS - 1])

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacificSet and (r, c) in atlanticSet:
                    res.append([r, c])

        return res