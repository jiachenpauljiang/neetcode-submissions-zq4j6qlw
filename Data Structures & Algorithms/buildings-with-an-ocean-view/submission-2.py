class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = deque()
        curMax = heights[-1]
        res.appendleft(len(heights) - 1)

        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > curMax:
                curMax = heights[i]
                res.appendleft(i)
        
        return [*res]