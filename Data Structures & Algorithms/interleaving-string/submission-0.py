class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}
        
        def backtracking(i, j):
            k = i + j

            if k == len(s3):
                return True
            
            if (i, j) in memo:
                return memo[(i, j)]

            result = False
            
            if i < len(s1) and s1[i] == s3[k]:
                result = backtracking(i + 1, j)
            
            if not result and j < len(s2) and s2[j] == s3[k]:
                result = backtracking(i, j + 1)
            
            memo[(i, j)] = result
            return result
        return backtracking(0, 0)