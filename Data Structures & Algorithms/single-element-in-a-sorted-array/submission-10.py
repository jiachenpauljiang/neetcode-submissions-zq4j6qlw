class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Logic:
        Before the single element, every pair starts with even index
        After the single element, every pair starts with odd index
        """

        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2

            # ensure m is even so that we can check neighbors
            if m % 2 != 0:
                m -= 1
            
            if nums[m] == nums[m + 1]:
                # the single element is in the right half, update left pointer
                l = m + 2
            else:
                r = m
        return nums[l]