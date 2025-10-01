class Solution:
    # def uniquePathsUtil(self, m: int, n: int, i, j) -> int:
    #     if i >= m or j >= n:
    #         return 0
        
    #     if i == m-1 and j == n-1:
    #         return 1
        
    #     return self.uniquePathsUtil(m, n, i, j+1) + self.uniquePathsUtil(m, n, i+1, j)

    def uniquePaths(self, m: int, n: int) -> int:
        # return self.uniquePathsUtil(m, n, 0, 0)
        dp = []
        for i in range(0, m):
            dp.append([])
            for j in range(0, n):
                dp[i].append(0)
                if i == 0 or j == 0:
                    dp[i][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]

  
        