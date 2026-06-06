class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2

            if m % 2 != 0:
                # force m to be even to check neighbors
                m -= 1
            
            if nums[m] == nums[m + 1]:
                # the single element is between m and r 
                l = m + 2
            else:
                r = m
            
        return nums[l]