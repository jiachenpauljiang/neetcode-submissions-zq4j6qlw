class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # [-1,0,1,2,-1,-4] -> [-4,-1,-1,0,1,2]
        for i in range(len(nums)):
            a = nums[i] # the current fixed number
            if a > 0:
                break
            if i > 0 and a == nums[i-1]: continue
            
            l = i + 1
            r = len(nums) - 1

            while l < r:
                sum = nums[l] + nums[r] + a
                if sum == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1

        return res