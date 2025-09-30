class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prev = nums[0]
        curr = max_num = max(nums[0], nums[1])


        for i in range(2, len(nums)):
            curr_max = max(nums[i] + prev, curr)
            prev = curr
            curr = curr_max
            if max_num < curr_max:
                max_num = curr_max
        return max_num

        