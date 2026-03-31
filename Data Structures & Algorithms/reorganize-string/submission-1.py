class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)

        maxHeap = [(-count, character) for character, count in counts.items()]
        heapq.heapify(maxHeap)

        res = ""
        prev = None
        while maxHeap:
            count, character = heapq.heappop(maxHeap)
            res += character
            count += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if count != 0:
                prev = (count, character)
        if len(res) == len(s):
            return res
        else:
            return ""