class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = maxCount = 0
        for i in range(len(nums)):
            count[nums[i]] += 1
            if maxCount < count[nums[i]]:
                res = nums[i]
                maxCount = count[nums[i]]
        return res 