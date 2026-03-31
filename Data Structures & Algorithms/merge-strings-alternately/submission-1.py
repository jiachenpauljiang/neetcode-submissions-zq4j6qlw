class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len, word2_len = len(word1), len(word2)
        result_len = min(word1_len, word2_len)

        res = ""
        for i in range(result_len):
            res = res + word1[i] + word2[i]
        if word1_len == word2_len:
            return res

        if word1_len > result_len:
            res = res + word1[result_len:]
        else:
            res = res + word2[result_len:]
            
        return res
