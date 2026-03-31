class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(index, curList, total):
            if total == target:
                res.append(curList.copy())
                return

            for i in range(index, len(nums)):
                if total + nums[i] <= target:
                    curList.append(nums[i])
                    dfs(i, curList, total + nums[i])
                    curList.pop()

        dfs(0, [], 0)
        return res    