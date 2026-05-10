class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        instead of removing the minimum number of intervals, 
        we can calculate the maximum of non-overlapping intervals 
        then the answer becomes len(intervals) - maximum of non-overlapping intervals

        define dp[], where dp[i] means the number of max number of non-overlapping intervals up to index i
        """
        
        intervals.sort(key=lambda x: x[1])
        dp = [0] * len(intervals)

        for i in range(len(intervals)):
            dp[i] = 1
            for j in range(i):
                if intervals[j][1] <= intervals[i][0]:
                    # if the previous interval ending time is smaller than the current interval start time
                    # meaning non overlap
                    dp[i] = max(dp[i], 1 + dp[j])
        return len(intervals) - max(dp)