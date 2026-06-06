class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False

        memo = {}
        
        def dfs(i, target):
            """
            For the first i numbers to reach target, there are 2 options:
            1. If the first i - 1 numbers can already reach target, the first i numbers can always reach target 
            2. If the first i - 1 numbers can reach target - nums[i], the first i numnbers can reach target 
            """
            if i == len(nums):
                return target == 0
            
            if target < 0:
                return False

            if (i, target) in memo:
                return memo[(i, target)]

            memo[(i, target)] = dfs(i + 1, target) or dfs(i + 1, target - nums[i])

            return memo[(i, target)]

        return dfs(0, sum(nums) // 2)