class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2

            # forcing m to be even so that we can check the neighboring numbers
            if m % 2 != 0:
                m -= 1
            
            if nums[m] == nums[m + 1]:
                # the single element is in the right half 
                l = m + 2
            else:
                # the single element is in the left half 
                r = m
        return nums[r]