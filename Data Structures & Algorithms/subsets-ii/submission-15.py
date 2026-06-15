class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        def backtrack(i, cur):
            # the ith element in nums, the current subset 
            
            if i == len(nums):
                res.append(cur.copy())
                return
            
            cur.append(nums[i])
            backtrack(i + 1, cur)
            cur.pop()

            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            backtrack(i + 1, cur)

        backtrack(0, [])
        return res