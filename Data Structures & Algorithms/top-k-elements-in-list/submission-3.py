class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        {num, freq}
        [[], [], [], []] ==> [[], [numbers with freq 1], [numbers with freq 2], ... ]
        """
        count = {} 
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num, count in count.items():
            freq[count].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res