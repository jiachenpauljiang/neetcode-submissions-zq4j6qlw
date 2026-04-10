class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        MOD = 1000000007
        res = 0

        for i in range(len(nums)):
            if nums[i] * 2 > target:
                break
            
            l, r = i, len(nums) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[i] + nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            count = pow(2, r - i, MOD)
            res = (res + count) % MOD
        return res