class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Before the single element, every pair starts on an even index 
        After the single element, every pair starts on an odd index 
        """

        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2

            # force m to be even so that we can determine if it's a pair 
            if m % 2 != 0:
                m -= 1

            if nums[m] == nums[m + 1]:
                # the single element is after m 
                l = m + 2
            else:
                r = m
            
        return nums[l]