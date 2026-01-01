class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total_sum = 0
        for i in range(len(nums)):
            total_sum += nums[i]
        
        if total_sum%2 :
            return False
        
        total_sum: int = total_sum // 2

        dp = []

        for i in range(total_sum+1):
            dp.append([])

        
        for i in range(total_sum+1):
            for j in range(len(nums)):
                if i == 0:
                    dp[i].append(True)
                    continue
                is_true = False
                if j == 0:
                    is_true = i == nums[j]                    
                else:
                    is_true = True if dp[i][j-1]  or (i-nums[j] >= 0 and dp[i-nums[j]][j-1])else False

                dp[i].append(is_true)
        # print('dp:', dp)
        return dp[total_sum][len(nums)-1]

        