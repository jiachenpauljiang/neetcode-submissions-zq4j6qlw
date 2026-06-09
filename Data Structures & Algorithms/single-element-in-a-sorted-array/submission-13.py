class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2

            # force m to be even so that we can compare neighbors
            if m % 2 != 0:
                m -= 1
            
            if nums[m] == nums[m + 1]:
                # the single element is to the right of nums[m + 1]
                l = m + 2
            else:
                r = m
        
        return nums[l]