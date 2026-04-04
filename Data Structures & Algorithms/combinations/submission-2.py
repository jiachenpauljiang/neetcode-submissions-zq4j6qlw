class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(i, combination):
            if i > n:
                if len(combination) == k:
                    res.append(combination.copy())
                return 

            combination.append(i)
            backtrack(i + 1, combination)
            combination.pop()
            backtrack(i + 1, combination)
        backtrack(1, [])
        return res
