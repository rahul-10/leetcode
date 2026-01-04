class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final: list[list[int]] = []

        def dfs(nums: list[int], index):
            if index >= len(nums):
                final.append(nums.copy())
                return 

            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                dfs(nums, index+1)
                nums[i], nums[index] = nums[index], nums[i]

        dfs(nums, 0)    
        return final

        