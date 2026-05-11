class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def backtrack(nums, target, index, currentSum):
            if index == len(nums):
                return 1 if target == currentSum else 0
            
            add = backtrack(nums, target, index + 1, currentSum + nums[index])
            subtract = backtrack(nums, target, index + 1, currentSum - nums[index])

            return add + subtract

        return backtrack(nums, target, 0, 0)