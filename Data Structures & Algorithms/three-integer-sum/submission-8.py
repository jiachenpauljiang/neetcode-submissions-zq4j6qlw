class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        [-1,0,1,2,-1,-4]

        [-4, -1, -1, 0, 1, 2]
          a
              i            j
        """
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0: break

            if i > 0 and num == nums[i-1]: continue # deal with duplicated first number 

            l = i + 1
            r = len(nums) - 1
            while l < r:
                three_sum = num + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                
        return res