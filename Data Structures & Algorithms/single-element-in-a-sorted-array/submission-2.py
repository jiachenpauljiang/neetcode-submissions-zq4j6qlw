class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        Observation: 
        Before the single element, the pair starts with even index.
        After the single element, the pair starts with odd index.
        """

        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            # ensure mid is even 
            if mid % 2 != 0:
                mid  = mid - 1
            
            if nums[mid] == nums[mid + 1]:
                # the single element is after mid 
                l = mid + 2
            else:
                # the single element is before or at mid 
                r = mid
        return nums[l] 