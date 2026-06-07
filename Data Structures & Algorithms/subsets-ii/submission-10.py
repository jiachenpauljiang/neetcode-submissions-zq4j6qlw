class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(start, cur_subset):
            res.append(cur_subset.copy())

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                cur_subset.append(nums[i])
                backtrack(i + 1, cur_subset)
                cur_subset.pop()
        
        backtrack(0, [])
        return res 