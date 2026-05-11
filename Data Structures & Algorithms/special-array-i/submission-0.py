class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        for i in range(1, len(nums)):
            num1, num2 = nums[i-1], nums[i]

            if num1 % 2 == 0 and num2 % 2 == 0:
                return False
            
            if num1 % 2 != 0 and num2 % 2 != 0:
                return False
        return True