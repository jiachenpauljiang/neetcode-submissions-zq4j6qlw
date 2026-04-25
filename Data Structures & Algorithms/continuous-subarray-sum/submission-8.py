class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums) - 1):
            curSum = nums[i]
            for j in range(i + 1, len(nums)):
                curSum += nums[j]
                if (curSum % k == 0):
                    return True
        return False