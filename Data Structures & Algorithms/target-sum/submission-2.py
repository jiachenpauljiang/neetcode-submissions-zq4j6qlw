class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        index_currentSum_map = defaultdict(int)

        def backtrack(nums, target, index, currentSum):
            if index == len(nums):
                return 1 if target == currentSum else 0

            key = f"{index}-{currentSum}"
            if key in index_currentSum_map:
                return index_currentSum_map.get(key)                    
            
            add = backtrack(nums, target, index + 1, currentSum + nums[index])
            subtract = backtrack(nums, target, index + 1, currentSum - nums[index])

            index_currentSum_map[key] = add + subtract

            return add + subtract

        return backtrack(nums, target, 0, 0)