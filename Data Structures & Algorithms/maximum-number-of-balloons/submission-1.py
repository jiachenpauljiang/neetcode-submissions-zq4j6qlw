class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_dict = defaultdict(int)

        for c in text:
            if c in "balloon":
                balloon_dict[c] += 1
        
        for c in "balon":
            if c not in balloon_dict:
                return 0
        
        return min(
            balloon_dict["b"],
            balloon_dict["a"],
            balloon_dict["l"] // 2,
            balloon_dict["o"] // 2,
            balloon_dict["n"]
        )