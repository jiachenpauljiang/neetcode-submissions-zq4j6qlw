class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, curList, total):
            if total == target:
                res.append(curList.copy())
                return
            
            if index >= len(nums) or total > target:
                return
            
            curList.append(nums[index])
            dfs(index, curList, total + nums[index])

            curList.pop()
            dfs(index + 1, curList, total)

        
        dfs(0, [], 0)
        return res