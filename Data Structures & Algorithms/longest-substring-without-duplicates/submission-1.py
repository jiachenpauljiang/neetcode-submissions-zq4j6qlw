class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        unique_char_set = set()
        l = 0
        for r in range(len(s)):
            while s[r] in unique_char_set:
                unique_char_set.remove(s[l])
                l += 1
            unique_char_set.add(s[r])
            res = max(res, r - l + 1)
        return res