class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, c in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + c < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + c
            prices = tmpPrices
        
        if prices[dst] == float("inf"):
            return -1
        else:
            return prices[dst]