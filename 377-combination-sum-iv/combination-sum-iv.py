class Solution:
    # def combinationSum4Util(self, nums: List[int], target: int, dp: List[int]) -> int:
    #     if target < 0:
    #         return 0
    #     if target == 0:
    #         return 1
        
    #     if dp[target] >= 0:
    #         return dp[target]

    #     current_sum = 0
        
    #     for i in range(0, len(nums)):
    #         current_sum += self.combinationSum4Util(nums, target-nums[i], dp)
        
    #     dp[target] = current_sum
    #     return current_sum

    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = []
        for i in range(0, target+1):
            dp.append(0)
        # return self.combinationSum4Util(nums, target, dp)
        dp[0] = 1
        for index in range(1, target+1):
            current_sum = 0
            for i in range(0, len(nums)):
                current_sum += dp[index-nums[i]] if index-nums[i] >= 0 else 0
            dp[index] = current_sum

        return dp[target]