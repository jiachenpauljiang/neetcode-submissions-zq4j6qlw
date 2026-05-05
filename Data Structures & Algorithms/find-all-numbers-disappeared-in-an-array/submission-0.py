class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        correct_set = set(range(1, len(nums) + 1))
        given_set = set(nums)

        return list(correct_set.difference(given_set))