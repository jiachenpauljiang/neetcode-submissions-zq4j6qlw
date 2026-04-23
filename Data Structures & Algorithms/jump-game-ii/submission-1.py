class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [100000] * len(nums)
        dp[-1] = 0

        for i in range(len(nums) - 2, -1, -1):
            end = min(nums[i] + i + 1, len(nums))
            for j in range(i + 1, end):
                dp[i] = min(dp[i], dp[j] + 1)
        return dp[0]