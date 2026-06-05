class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        max_so_far = heights[-1]

        res = deque()

        res.append(len(heights) - 1)

        for i in range(len(heights) - 2, -1, -1):
            cur_height = heights[i]

            if cur_height > max_so_far:
                res.appendleft(i)
                max_so_far = cur_height
        
        return [*res]
