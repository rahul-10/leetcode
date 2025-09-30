class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp: List[int] = []
        final = -1
        for idx, value in enumerate(nums):
            j = idx-1
            curr_max = -1
            while j >= 0:
                if nums[j] < nums[idx]:
                    curr_max = max(curr_max, 1 + dp[j])
                j = j-1

            dp.append( 1 if curr_max <= 0 else curr_max )
            final = max(final, dp[idx])
        return final


        