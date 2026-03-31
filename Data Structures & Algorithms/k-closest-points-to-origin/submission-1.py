from _heapq import heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        [[2,0,2],[2,2,0],[sqrt(2),2,2]]
        """
        for point in points:
            distance = (point[0] ** 2 + point[1] ** 2)
            point.insert(0, int(distance))
        
        heapq.heapify(points)

        res = []
        for i in range(k):
            point = heappop(points)
            point.pop(0)
            res.append(point)
            print(res)

        return res