class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        def dfs(start, cur):
            if start == len(nums):
                res.append(cur.copy())
                return
            
            cur.append(nums[start])
            dfs(start + 1, cur)
            cur.pop()

            while start + 1 < len(nums) and nums[start + 1] == nums[start]:
                start += 1
            dfs(start + 1, cur)
        dfs(0, [])
        return res