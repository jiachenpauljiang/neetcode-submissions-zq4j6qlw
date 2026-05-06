class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = {}
        dp[0] = [0, 1, 0]
        for i in range(1, rowIndex + 1):
            dp[i] = [0] * (i + 3)
        
        """
        i = 0: [0,1,0]
        i = 1: [0,1,1,0]
        i = 2: [0,1,2,1,0]
        i = 3: [0,1,3,3,1,0]
        """

        for i in range(1, rowIndex + 1):
            for j in range(1, i + 2):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp[rowIndex][1:rowIndex+2]