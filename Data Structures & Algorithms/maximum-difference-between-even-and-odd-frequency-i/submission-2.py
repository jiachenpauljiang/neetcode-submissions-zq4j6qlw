class Solution:
    def maxDifference(self, s: str) -> int:
        frequency_map = defaultdict(int)

        for c in s:
            frequency_map[c] += 1
        max_odd = max(val for val in frequency_map.values() if val % 2 != 0)
        max_even = min(val for val in frequency_map.values() if val % 2 == 0)

        return max_odd - max_even