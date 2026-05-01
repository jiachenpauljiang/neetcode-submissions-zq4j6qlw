class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == 0:
                leftSum = 0
                rightSum = sum(nums[1:])
                if leftSum == rightSum:
                    return i
            elif i == len(nums) - 1:
                rightSum = 0
                leftSum = sum(nums[:i])
                if leftSum == rightSum:
                    return i
            else:
                leftSum = sum(nums[:i+1])
                rightSum = sum(nums[i:])
                print(f"leftSum: {leftSum}")
                if leftSum == rightSum:
                    return i
        return -1