class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        if total_sum % 2 != 0:
            return False
        
        sub_sum = total_sum // 2

        dp = [[False] * (sub_sum + 1) for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            dp[i][0] = True
        
        for i in range(1, len(nums) + 1):
            for s in range(1, sub_sum + 1):
                if dp[i - 1][s]:
                    dp[i][s] = True
                elif s >= nums[i - 1] and dp[i - 1][s - nums[i - 1]]:
                    dp[i][s] = True
        return dp[-1][-1]