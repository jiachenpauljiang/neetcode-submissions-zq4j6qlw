class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Since the integers are all positive, we use a sliding window. 
        We keep expanding towards right until the sum exceeds target. 
        Then, we start shrinking the left pointer. 
        When we reach a point of the sum smaller than target, the previous window is the result.
        """
        l = 0

        window_sum = 0

        min_len = float('inf')

        for r in range(len(nums)):
            window_sum += nums[r]

            while window_sum >= target:
                min_len = min(min_len, r - l + 1)
                window_sum -= nums[l]
                l += 1
        
        if min_len == float('inf'):
            return 0
        else:
            return min_len