class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Start with index i
            Find 2 numbers that sum up to -nums[i] starting from index i + 1
        """
        nums.sort()
        res = []

        for i in range(len(nums)):

            curFixedNum = nums[i]
            # if curFixedNum is positive, there is no reason to continue  
            if curFixedNum > 0: 
                break
            
            # skip duplicated
            if i > 0 and nums[i] == nums[i-1]: 
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = curFixedNum + nums[l] + nums[r]
                if sum == 0:
                    res.append([curFixedNum, nums[l], nums[r]])
                    l += 1
                    r -= 1  
                    while l < r and nums[l] == nums[l-1]: 
                        l += 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1

        return res 