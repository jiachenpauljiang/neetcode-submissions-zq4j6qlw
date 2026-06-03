class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        If sum(nums) is odd, return False

        The goal is to find a subset of nums so that the sum can be sum(nums) // 2
        """

        if sum(nums) % 2 != 0:
            return False

        memo = {}
        
        def dfs(i, target):
            """
            Checks if we can form a sum of target using the first i numbers in nums
            """
            if i == len(nums):
                return target == 0
            
            if target == 0:
                return True
            
            if target < 0:
                return False
            
            if (i, target) in memo:
                return memo[(i, target)]
            
            memo[(i, target)] = dfs(i + 1, target) or dfs(i + 1, target - nums[i])
            
            return memo[(i, target)]
        
        return dfs(0, sum(nums) // 2)