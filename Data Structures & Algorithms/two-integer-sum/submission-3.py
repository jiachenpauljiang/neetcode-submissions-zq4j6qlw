class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for index, number in enumerate(nums):
            diff = target - number
            if diff in prevMap:
                return [prevMap[diff], index]
            prevMap[number] = index