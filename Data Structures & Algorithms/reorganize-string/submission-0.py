from _heapq import heapify
class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        heap = [[-count, item] for item, count in counts.items()]

        heapify(heap)

        res = ""
        prev = None
        while heap or prev:
            if prev and not heap:
                return ""
            cnt, char = heapq.heappop(heap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(heap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, char]
        
        return res