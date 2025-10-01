class Solution:
    def robUtil(self, nums: List[int], start, end, final) -> int:
        prev = 0
        curr = nums[start]
        start += 1
        final = max(final, curr)
        while(start <= end):
            local_max = max(prev + nums[start], curr)
            if final < local_max:
                final = local_max
            prev = curr
            curr = local_max
            start += 1
        return final

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        final = self.robUtil(nums, 0, len(nums) - 2, 0)

        return self.robUtil(nums, 1, len(nums) - 1, final)
        
        
        


        