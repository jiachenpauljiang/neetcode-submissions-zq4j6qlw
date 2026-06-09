class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        memo = {}
        
        def dfs(i, target):
            """
            If we can form a sum of target using the first i numbers
            """
            if target == 0:
                return True
            
            if i == len(nums):
                return target == 0
            
            if (i, target) in memo:
                return memo[(i, target)]
            
            # either we take the current number, or we don't take the current number 
            memo[(i, target)] = dfs(i + 1, target) or dfs(i + 1, target - nums[i])
            return memo[(i, target)]
        return dfs(0, sum(nums) // 2)