class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums_set = set(nums)

        for num in nums_set:
            if nums.count(num) % 2 != 0:
                return False
        return True