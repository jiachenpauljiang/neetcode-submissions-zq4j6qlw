class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(capacity):
            ship = 1
            curr_capacity = capacity
            for w in weights:
                if w > curr_capacity:
                    ship += 1
                    curr_capacity = capacity
                curr_capacity -= w
            if ship <= days:
                return True
            else:
                return False

        while l <= r:
            cap = l + (r - l) // 2
            if canShip(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1
        return res