class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustedByOthers = defaultdict(int)
        trustOthers = defaultdict(int)

        for i, j in trust:
            trustOthers[i] += 1
            trustedByOthers[j] += 1
        
        for i in range(1, n + 1):
            if trustedByOthers[i] == n - 1 and not trustOthers[i]: 
                return i
        return -1