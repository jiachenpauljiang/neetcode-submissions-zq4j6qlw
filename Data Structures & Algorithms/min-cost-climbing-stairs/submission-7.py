class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mem = [-1] * (len(cost))

        def dfs(i):
            if i >= len(cost): return 0
            if mem[i] != -1: return mem[i]
            mem[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return mem[i]
        return min(dfs(0), dfs(1))