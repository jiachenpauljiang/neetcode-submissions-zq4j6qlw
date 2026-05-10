class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # initially set both flag to True 
        increasing, decreasing = True, True

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                increasing = False
            if nums[i] > nums[i - 1]:
                decreasing = False
        return increasing or decreasing