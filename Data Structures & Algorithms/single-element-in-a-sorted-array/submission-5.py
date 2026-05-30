class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        The pairs before the single element starts with even index.
        The pairs after the single element starts with oddi ndex
        """

        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2

            # force m to be even to check pairs 
            if m % 2 != 0:
                m -= 1
            
            # check the pairs 
            if nums[m] == nums[m+1]:
                # the single element is to the right
                l = m + 2
            else:
                # the single element is m or to the left
                r = m
        return nums[l]