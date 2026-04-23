class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 0 or not nums:
            return 0
        # dp[i] means the minimum jump from index i to the last num 
        dp = [100000] * len(nums)
        dp[-1] = 0

        for i in range(len(nums) - 2, -1, -1):
            end = min(len(nums), i + nums[i] + 1)
            for j in range(i + 1, end):
                dp[i] = min(dp[i], dp[j] + 1)
        return dp[0]