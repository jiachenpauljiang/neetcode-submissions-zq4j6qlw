class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        M, N = len(grid), len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        queue = deque() # a queue that holds all the treasure chests 
        for m in range(M):
            for n in range(N):
                if grid[m][n] == 0:
                    queue.append((m, n))
        dist = 1
        while queue:
            for _ in range(len(queue)):

                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc 

                    if 0 <= nr < M and 0 <= nc < N and grid[nr][nc] == 2147483647:
                        grid[nr][nc] = dist
                        queue.append((nr, nc))
            dist += 1