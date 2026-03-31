class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for record in operations:
            if record == "+":
                prev1, prev2 = res[-1], res[-2]
                res.append(int(prev1) + int(prev2))
            elif record == "C":
                res.pop()
            elif record == "D":
                lastElement = res[-1]
                res.append(lastElement * 2)
            else:
                res.append(int(record))
        return sum(res)