class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
         intervals.sort(key=lambda x: x[1])
         n = len(intervals)
         dp = [0] * n # dp[i] means the maximum number of non overlapping intervals we can keep ending at interval i

         for i in range(n):
            dp[i] = 1
            for j in range(i):
                if intervals[j][1] <= intervals[i][0]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    
         return n - max(dp)