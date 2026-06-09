class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        # construct a 2D table, where rows is the ith number, columns is the target sums 
        dp = [[False] * (sum(nums) // 2 + 1) for _ in range(len(nums) + 1)]

        # since 0 can be formed by any number, the first column is all True

        for i in range(len(nums) + 1):
            dp[i][0] = True
        
        for r in range(1, len(nums) + 1):
            for c in range(1, sum(nums) // 2 + 1):
                # start to fill in the dp table
                # if dp[r - 1][c] is True, then dp[r][c] is True
                if dp[r - 1][c]:
                    dp[r][c] = True
                elif c - nums[r - 1] >= 0:
                    dp[r][c] = dp[r - 1][c - nums[r - 1]]
        
        return dp[-1][-1]