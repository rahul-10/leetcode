class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr_position = 0
        
        for i in range(0, len(nums)):
            if nums[i] == 0 and curr_position <= i:
                break
            
            curr_position = max(curr_position, nums[i] + i)
        
        if curr_position >= len(nums)-1:
            return True
        return False