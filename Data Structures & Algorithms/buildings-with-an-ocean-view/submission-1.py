class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        cur_max = heights[-1]
        res = deque()
        res.append(len(heights) - 1)

        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > cur_max:
                cur_max = heights[i]
                res.appendleft(i)
        
        return [*res]