class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        def backtrack(start, current):
            if start == len(nums):
                res.append(current.copy())
                return
            
            current.append(nums[start])
            backtrack(start + 1, current)
            current.pop()

            while start + 1 < len(nums) and nums[start] == nums[start + 1]:
                start += 1

            backtrack(start + 1, current)
        
        backtrack(0, [])
        return res