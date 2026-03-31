class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        queue = []

        for k, v in enumerate(temperatures):
            while queue:
                p_i, p_t = queue[-1][0], queue[-1][1]
                if v > p_t:
                    res[p_i] = k - p_i
                    queue.pop()
                else: # v<= queue
                    break
            queue.append([k, v])
        
        return res 