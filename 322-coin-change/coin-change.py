class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp: list[int] = []
        dp.append(0)
        
        for i in range(1, amount+1):
            curr = -1
            for j in range(len(coins)):
                if i - coins[j] < 0 or dp[i - coins[j]] == -1:
                    continue
                if curr >= 0 :
                    curr = min(curr, 1 + dp[i - coins[j]])
                else:
                    curr = 1 + dp[i - coins[j]]
            dp.append(curr)
        # print('dp: ', dp)
        return dp[-1]


        