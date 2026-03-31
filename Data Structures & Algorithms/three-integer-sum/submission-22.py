class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for index, num in enumerate(nums):
            if num > 0: break
            if index > 0 and num == nums[index - 1]: continue

            l, r = index + 1, len(nums) - 1

            while l < r:
                currentSum = num + nums[l] + nums[r]

                if currentSum == 0:
                    result.append([num, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif currentSum < 0:
                    l += 1
                else:
                    r -= 1
            
        return result