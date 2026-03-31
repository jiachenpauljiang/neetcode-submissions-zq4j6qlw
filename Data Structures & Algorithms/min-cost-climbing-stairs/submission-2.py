class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev1 = prev2 = 0

        for stair in range(2, len(cost) + 1):
            curCost = min(prev1 + cost[stair - 1], prev2 + cost[stair - 2])
            prev2 = prev1
            prev1 = curCost
        
        return prev1