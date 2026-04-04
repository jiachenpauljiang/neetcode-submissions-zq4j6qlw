class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(permutation):
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return 

            for num in nums:
                if num in permutation:
                    continue
                permutation.append(num)
                backtrack(permutation)
                permutation.pop()
        backtrack([])
        return res