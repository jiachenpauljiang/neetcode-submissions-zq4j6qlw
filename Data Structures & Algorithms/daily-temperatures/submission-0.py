class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for day in range(len(temperatures)):
            while stack and temperatures[day] > stack[-1][1]:
                curIndex, curTemp = stack.pop()
                res[curIndex] = day - curIndex
            stack.append((day, temperatures[day]))
        return res 



        """
        [(1, 38), (2, 30), (3, 36)]
        []
        """