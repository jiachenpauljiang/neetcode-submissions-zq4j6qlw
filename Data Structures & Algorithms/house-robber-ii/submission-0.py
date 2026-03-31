class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        For each house, there are 2 options:
        Option 1: rob current house, but skip next house
        Option 2, skip current house, and rob next house 

        You cannot rob nums[-1] and nums[0]

        Split into 2 cases: rob nums[0:n-2], rob nums[1:n-1]
        """

        if len(nums) == 1: 
            return nums[0]
        return max(self.dp(nums[: -1]), self.dp(nums[1:]))
        

    def dp(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        res = [0] * len(nums)
        res[0] = nums[0]
        res[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            res[i] = max(res[i - 1], res[i - 2] + nums[i])
        
        return res[-1]
