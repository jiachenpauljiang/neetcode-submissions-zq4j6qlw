class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount == 0: return 0
            if amount in memo: return memo[amount]

            result = 1e9

            for coin in coins:
                if amount - coin >= 0:
                    result = min(result, 1 + dfs(amount - coin))
            
            memo[amount] = result
            return result
        
        if dfs(amount) != 1e9:
            return dfs(amount)
        else:
            return -1