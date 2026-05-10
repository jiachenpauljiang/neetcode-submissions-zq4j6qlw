class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        diff_set = set()
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                diff_set.add(1)
            elif nums[i] < nums[i-1]:
                diff_set.add(-1)
            else:
                diff_set.add(0)
        
        if 1 in diff_set and -1 in diff_set:
            return False
        return True