class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        # construct a 2D DP table, row is 0 to ith number in nums, col is 0 to sum(nums) // 2 + 1 
        dp = [[False] * (sum(nums) // 2 + 1) for _ in range(len(nums) + 1)]

        # mark the first column as True because we can reach 0 with anything
        # the first row is already False except (0, 0) because 0 cannor reach anything beyond 0
        for i in range(len(nums) + 1):
            dp[i][0] = True
        
        for i in range(1, len(nums) + 1):
            for s in range(1, sum(nums) // 2 + 1):
                if dp[i - 1][s]:
                    # if the previous numbers can make up s, we can too by not taking the current number 
                    dp[i][s] = True
                elif s - nums[i - 1] >= 0:
                    # otherwise, if taking the current number can still keep s positive, we can check if taking this number can exactly match s
                    dp[i][s] = dp[i - 1][s - nums[i - 1]]
        return dp[-1][-1]
                