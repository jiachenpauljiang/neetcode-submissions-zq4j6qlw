class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """
        O(logn) implies binary search 

        Before the single element, the pair starts on an even index 
        After the single element, the pair starts on an odd index 
        """
        left, right = 0, len(nums) - 1

        while left < right:
            middle = left + (right - left) // 2

            # force middle to be even 
            if middle % 2 != 0:
                middle -= 1
            
            if nums[middle] == nums[middle + 1]:
                # the single element is to the right 
                left = middle + 2
            else:
                right = middle
        return nums[left]