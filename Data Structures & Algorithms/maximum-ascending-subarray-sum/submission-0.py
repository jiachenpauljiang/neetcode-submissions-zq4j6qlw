class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        res = 0
        curMaxSum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curMaxSum += nums[i]
                print("Number is", nums[i], ", incrementing, curMaxSum =", curMaxSum)
            else:
                res = max(res, curMaxSum)
                curMaxSum = nums[i]
                print("Number is", nums[i], ", resetting, curMaxSum =", curMaxSum)

        return max(res, curMaxSum)