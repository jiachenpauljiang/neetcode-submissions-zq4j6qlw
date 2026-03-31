class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True 
        
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return checkPalindrome(s[l + 1: r + 1]) or checkPalindrome(s[l: r])
            l += 1
            r -= 1
        return True
