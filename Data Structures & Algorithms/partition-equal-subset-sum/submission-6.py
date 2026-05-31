class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        The sum of nums must be even
        If we can find one subset that sums up to sum(nums) // 2, then we don't need to check the other half 
        """

        if sum(nums) % 2 != 0:
            return False
        
        memo = {}

        # search for the ith element in nums and see if we can form to sum target
        def dfs(i, target):
            if i == len(nums):
                return target == 0
            
            if target < 0:
                return False
            
            if (i, target) in memo:
                return memo[(i, target)]
            
            memo[(i, target)] = dfs(i + 1, target) or dfs(i + 1, target - nums[i])
            return memo[(i, target)]
        
        return dfs(0, sum(nums) // 2)