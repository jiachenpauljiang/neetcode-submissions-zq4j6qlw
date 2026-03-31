class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {")": "(", "]": "[", "}": "{"}

        for c in s:
            # if it's a closing bracket
            if stack and c in bracket_map:
                if stack[-1] == bracket_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0