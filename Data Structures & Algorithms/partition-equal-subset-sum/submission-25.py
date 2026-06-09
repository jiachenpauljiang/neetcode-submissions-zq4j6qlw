class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        # construct a dp table where row represents every number in nums, column represents every number from 0 to sum(nums) // 2
        # each cell == whether we can construct to a sum using the first i numbers 

        dp = [[False] * (sum(nums) // 2 + 1) for _ in range(len(nums) + 1)]

        # The first column should always be True because any number can form a sum of 0
        for i in range(len(nums) + 1):
            dp[i][0] = True
        
        for r in range(1, len(nums) + 1):
            for c in range(1, sum(nums) // 2 + 1):
                # If dp[r - 1][c] is True, dp[r][c] should be True as well
                # if dp[r - 1][c] is False, dp[r][c] could be True if the current number happen to bridge the gap between sum 
                if dp[r - 1][c]:
                    dp[r][c] = True
                elif c - nums[r - 1] >= 0:
                    dp[r][c] = dp[r - 1][c - nums[r - 1]]
        return dp[-1][-1]