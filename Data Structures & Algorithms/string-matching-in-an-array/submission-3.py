class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []

        for i in range(len(words)):
            curWord = words[i]
            print("curWord: " + curWord)
            for j in range(len(words)):
                if j == i:
                    continue
                if curWord in words[j]:
                    res.append(curWord)
                    break
        return res