class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        count_dict = defaultdict(int)
        minVal, maxVal = min(nums), max(nums)

        for val in nums:
            count_dict[val] += 1
        
        index = 0
        for val in range(minVal, maxVal + 1):
            while count_dict[val] > 0:
                nums[index] = val
                index += 1
                count_dict[val] -= 1
        return nums