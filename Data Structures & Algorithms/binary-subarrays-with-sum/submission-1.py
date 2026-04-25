class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        
        def helper(x):
            # count number of sub arrays where curSum <= x
            if x < 0: 
                return 0
            
            res = 0
            l = 0
            curSum = 0

            for i in range(len(nums)):
                curSum += nums[i]
                while curSum > x:
                    curSum -= nums[l]
                    l += 1
                res += (i - l + 1)
            return res
        return helper(goal) - helper(goal - 1)