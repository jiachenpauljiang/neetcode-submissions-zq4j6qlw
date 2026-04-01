class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        negated_nums = [-num for num in nums]
        heapq.heapify(negated_nums)
        res = []
        for i in range(len(nums)):
            num = heapq.heappop(negated_nums)
            res.insert(0, -num)
        return res