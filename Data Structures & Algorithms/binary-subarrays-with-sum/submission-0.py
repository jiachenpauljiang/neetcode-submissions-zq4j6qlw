class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            runningSum = 0
            for j in range(i, n):
                runningSum += nums[j]
                if runningSum == goal:
                    res += 1
        return res