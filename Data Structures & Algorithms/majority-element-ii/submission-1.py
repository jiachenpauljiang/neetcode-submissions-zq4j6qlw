class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter_map = Counter(nums)
        res = []
        # {num: freq}
        for key in counter_map:
            if counter_map[key] > len(nums) // 3:
                res.append(key)
        return res