class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = deque()
        res.appendleft(len(heights) - 1)

        tallest = heights[-1]

        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > tallest:
                tallest = heights[i]
                res.appendleft(i)
        
        return [*res]