class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Construct a 2D array dp[i][s], with dimension len(nums) + 1 and sum(nums) // 2 + 1
        where dp[i][s] is True/False meaning whether the first ith number in nums can sum up to s.
        """
        if sum(nums) % 2 != 0:
            return False
        
        dp = [[False] * (sum(nums) // 2 + 1) for _ in range(len(nums) + 1)]

        for i in range(len(nums) + 1):
            # mark the first column as True because any number can sum to 0 by not taking the number 
            dp[i][0] = True
        
        for i in range(1, len(nums) + 1):
            for s in range(1, sum(nums) // 2 + 1):
                # we have 2 options, take num[i - 1] or not take it
                if dp[i - 1][s]:
                    dp[i][s] = True
                elif s - nums[i - 1] >= 0:
                    dp[i][s] = dp[i - 1][s - nums[i - 1]]
        
        return dp[-1][-1]