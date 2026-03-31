class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            # for every char in the first string
            for s in strs:
                # for every string in strs
                if i == len(s) or s[i] != strs[0][i]:
                    return s[:i]
        return strs[0]