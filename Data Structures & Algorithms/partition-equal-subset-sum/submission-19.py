class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        dp = [[False] * (sum(nums) // 2 + 1) for _ in range(len(nums) + 1)]

        # In the above dp table, row is every number in nums. column is every number from 0 to sum(nums) // 2

        # the first column is always True because any number can form sum 0

        for i in range(len(nums) + 1):
            dp[i][0] = True
        
        for r in range(1, len(nums) + 1):
            for c in range(1, sum(nums) // 2 + 1):
                if dp[r - 1][c]:
                    dp[r][c] = True
                elif c - nums[r - 1] >= 0:
                    dp[r][c] = dp[r - 1][c - nums[r - 1]]
        
        return dp[-1][-1]