class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # [[], [], [], []] ==> [[], [numbers with 1 frequency], [numbers with 2 frequency], ...]
        # [[1], [2], [3]]

        num_count = {} # {number, frequency}
        frequency_lists = [[] for i in range(len(nums) + 1)]

        for num in nums:
            num_count[num] = 1 + num_count.get(num, 0)
        
        # {1: 1, 2: 2, 3: 3}

        for num, count in num_count.items():
            frequency_lists[count].append(num)
        
        # [[1], [2], [3]]
        res = []
        for i in range(len(frequency_lists) - 1, 0, -1):
            for j in frequency_lists[i]:
                
                res.append(j)

                if len(res) == k:
                    return res