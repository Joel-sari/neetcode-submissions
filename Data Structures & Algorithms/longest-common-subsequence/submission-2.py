class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows = len(text1)
        cols = len(text2)

        dp = []
        for r in range(rows + 1):
            dp.append([0] * (cols + 1))
        
        
        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if text1[r] == text2[c]:
                    #add 1 to the diagonal because you need the LCS for both text1 adn text2
                    #dp[r+1][c] is just the LCS for the next value of text1
                    #dp[r][c+1] is just the LCS for the next value of text2
                    #if you want both you need to increment both which is the diagonal
                    dp[r][c] = 1 + dp[r + 1][c+1]
                else:
                    # when the letters don't match, they can't pair with each other,
                    #at least one of them has to be skipped so we take the longest one
                    dp[r][c] = max(dp[r + 1][c], dp[r][c + 1])
        
        return dp[0][0]
