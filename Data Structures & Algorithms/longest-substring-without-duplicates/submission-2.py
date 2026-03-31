class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        seen_char_set = set()

        for r in range(len(s)):
            print("l, r =", l, r)
            print("set:", seen_char_set)
            while s[r] in seen_char_set:
                print("     Char ", s[r], "is seen in the set, removing", s[l])
                seen_char_set.remove(s[l])
                l += 1
                print("     l, r =", l, r)
                print("set:", seen_char_set)
            seen_char_set.add(s[r])
            print("set:", seen_char_set)
            res = max(res, len(seen_char_set))
        return res 