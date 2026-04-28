class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for i in range(len(details)):
            curPassenger = details[i]
            if (int(curPassenger[11:13]) > 60):
                res += 1
        return res