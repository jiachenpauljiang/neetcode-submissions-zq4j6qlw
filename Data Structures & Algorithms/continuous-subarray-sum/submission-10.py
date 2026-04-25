class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        reminder = {0: -1} # map remainder : ending index
        total = 0
        for index, value in enumerate(nums):
            total += value
            r = total % k

            if r not in reminder:
                reminder[r] = index
            else:
                arrLength = index - reminder[r]
                if arrLength >= 2:
                    return True
        return False