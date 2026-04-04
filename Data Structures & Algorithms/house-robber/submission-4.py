class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        lastLastOne = nums[0]
        lastOne = max(lastLastOne, nums[1])

        for i in range(2, len(nums)):
            cur = max(lastLastOne + nums[i], lastOne)
            lastLastOne = lastOne
            lastOne = cur

        return lastOne