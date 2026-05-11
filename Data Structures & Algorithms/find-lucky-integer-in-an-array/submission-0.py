class Solution:
    def findLucky(self, arr: List[int]) -> int:
        num_map = {}
        arr.sort(reverse=True)

        for i in range(len(arr)):
            if arr[i] not in num_map:
                num_map[arr[i]] = 1
            else:
                num_map[arr[i]] += 1
        
        for num, freq in num_map.items():
            if num == freq:
                return num
        return -1