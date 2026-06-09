class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        memo = {}
        
        def dfs(i, target):
            """
            Given the first i numbers, can we form a sum of target 

            2 options: take the current number, or not take it 
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