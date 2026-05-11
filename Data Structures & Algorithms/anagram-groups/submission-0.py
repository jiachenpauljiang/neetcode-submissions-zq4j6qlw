class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        strs_sorted = []
        for word in strs:
            strs_sorted.append("".join(sorted(word)))
        
        sorted_word_map = defaultdict(list)

        for i in range(len(strs_sorted)):
            sorted_word_map[strs_sorted[i]].append(strs[i])
        
        res = []
        for key, val in sorted_word_map.items():
            res.append(val)

        return res