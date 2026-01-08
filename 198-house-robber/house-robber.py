class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        x, y = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            x, y = y, max(nums[i] + x, y)
            
        return y
        