class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        #create extra row and column of 0s
        for i in range(m + 1):
            dp.append([0] * (n + 1))

        #set bottom right to 1
        dp[m - 1][n - 1] = 1


        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):

                dp[r][c] += dp[r][c + 1] + dp[r + 1][c]

        return dp[0][0]
                

                


