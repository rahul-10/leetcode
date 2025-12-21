class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result: List[int] = []
        curr = 1
        for idx, val in enumerate(nums):
            result.append(curr)
            curr = curr * val
        curr = 1
        for idx in range(len(nums)-1, -1, -1):
            result[idx] = curr * result[idx]
            curr = curr * nums[idx]

        return result
        
        