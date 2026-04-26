class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        sPointer = tPointer = 0

        while sPointer < len(s) and tPointer < len(t):
            if s[sPointer] == t[tPointer]:
                sPointer += 1
                tPointer += 1
            else:
                tPointer += 1
        
        if sPointer == len(s):
            return True
        else:
            return False