class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        N = len(grid)
        
        q = deque([(0, 0, 1)])
        visited = set((0, 0))
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        while q:
            r, c, res = q.popleft()
            if r == N - 1 and c == N - 1:
                return res
            
            for dr, dc in directions:
                newr, newc = r + dr, c + dc
                if newr >= 0 and newr < N and newc >= 0 and newc < N and (newr, newc) not in visited and grid[newr][newc] == 0:
                    q.append((newr, newc, res + 1))
                    visited.add((newr, newc))
        return -1