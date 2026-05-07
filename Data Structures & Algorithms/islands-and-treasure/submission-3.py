class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:


        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        def addCell(r, c):
            if 0 <= r < ROWS and 0 <= c < COLS and (r, c) not in visit and grid[r][c] != -1:
                visit.add((r, c))
                q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            
            dist += 1