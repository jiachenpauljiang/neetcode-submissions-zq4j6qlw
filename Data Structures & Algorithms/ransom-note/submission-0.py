class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        availMap = defaultdict(int)

        for c in magazine:
            availMap[c] += 1
        
        for c in ransomNote:
            if c in availMap and availMap[c] > 0:
                availMap[c] -= 1
            else:
                return False
        return True