class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        4 6 8 10
        1 3 5 7 9 10 
        0 1 2 3 4 5 6 7 8 9 10
        7 8 9 10
        """
        pairs = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pairs)[::-1]:
            stack.append((target - p) / s)
            if (len(stack) > 1 and stack[-1] <= stack[-2]):
                stack.pop()
        return len(stack)

