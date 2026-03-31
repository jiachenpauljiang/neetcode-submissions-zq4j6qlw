from _heapq import heapify
class Solution:
    def findMin(self, nums: List[int]) -> int:
        heapify(nums)
        return heapq.heappop(nums)