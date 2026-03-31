from _heapq import heapify
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        [-1, 0, 1, 2, 3]
        [-3, -2, -1, 0, 1]
        """
        nums_negated = [-i for i in nums]
        print(nums_negated)
        heapq.heapify(nums_negated)

        for i in range(k):
            res = heapq.heappop(nums_negated)
        
        return -1 * res