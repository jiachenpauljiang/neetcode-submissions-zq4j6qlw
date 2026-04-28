class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        globalMax = 0
        localMax = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                localMax += 1
            else:
                globalMax = max(globalMax, localMax)
                localMax = 0
        return max(localMax, globalMax)