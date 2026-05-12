class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def canSplit(starting_index):
            if starting_index == len(s):
                return True

            if starting_index in memo:
                return memo[starting_index]
            
            for word in wordDict:
                if s[starting_index : starting_index + len(word)] == word:
                    if canSplit(starting_index + len(word)):
                        memo[starting_index] = True
                        return True
            memo[starting_index] = False
            return False
            
        return canSplit(0)