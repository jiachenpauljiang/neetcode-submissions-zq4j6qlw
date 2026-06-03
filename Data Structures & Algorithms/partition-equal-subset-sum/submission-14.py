class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        # dp table, row is ith number, column is sum s from 0 
        dp = [[False] * (sum(nums) // 2 + 1) for _ in range(len(nums) + 1)]

        # any number can achieve sum 0 by not taking it 
        for i in range(len(nums) + 1):
            dp[i][0] = True
        
        for i in range(1, len(nums) + 1):
            for s in range(1, sum(nums) // 2 + 1):
                if dp[i - 1][s]:
                    dp[i][s] = True
                elif s - nums[i - 1] >= 0:
                    dp[i][s] = dp[i - 1][s - nums[i - 1]]
        
        return dp[-1][-1]