class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp: list[int] = []
        dp.append(nums[0])
        dp.append(max(nums[0], nums[1]))

        for i in range(2, len(nums)):
            dp.append(max(nums[i]+dp[i-2], dp[i-1]))
    
        return dp[len(nums)-1]
        
        