class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        def dfs(start, cur_subset):
            if start == len(nums):
                res.append(cur_subset.copy())
                return

            cur_subset.append(nums[start])
            dfs(start + 1, cur_subset)
            cur_subset.pop()

            while start + 1 < len(nums) and nums[start] == nums[start + 1]:
                start += 1
            
            dfs(start + 1, cur_subset)
        
        dfs(0, [])
        return res