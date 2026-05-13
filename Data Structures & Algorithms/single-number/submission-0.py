class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        numMap = defaultdict(int)

        for num in nums:
            numMap[num] += 1
        
        for num, freq in numMap.items():
            if freq == 1:
                return num