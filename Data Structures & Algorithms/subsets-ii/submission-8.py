class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        First sort the nums array so that we can check duplicates
        Then for each number we have 2 options, use it or not use it
        """
        res = []
        nums.sort()

        def backtrack(start, cur_subset):
            if start == len(nums):
                res.append(cur_subset.copy())
                return 

            cur_subset.append(nums[start])
            backtrack(start + 1, cur_subset)
            

            while start + 1 < len(nums) and nums[start + 1] == nums[start]:
                start += 1

            cur_subset.pop()
            backtrack(start + 1, cur_subset)
        
        backtrack(0, [])
        return res 