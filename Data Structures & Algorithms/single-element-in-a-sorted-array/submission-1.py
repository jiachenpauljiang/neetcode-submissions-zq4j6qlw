class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        The key observation is that before the single element, the same number pair starts with even index.
        After the single element, the same number pair starts with odd index.
        """
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            # force mid to be an even index in order to determine if we have past the single element 
            if mid % 2 == 1:
                mid -= 1
            
            if nums[mid] == nums[mid + 1]:
                # the single element is after mid, incrementing l pointer
                l = mid + 2
            else:
                r = mid
        return nums[l]