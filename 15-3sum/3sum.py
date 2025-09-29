class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = []
        for idx, value in enumerate(nums):
            if idx > 0 and value == nums[idx-1]:
                continue
            left = idx+1
            right = len(nums)-1

            while left < right:
                if nums[left] + nums[right] + value == 0:
                    res.append([value, nums[left], nums[right]])
                    right -= 1
                    while right > left and nums[right] == nums[right+1] :
                        right -= 1
                elif nums[left] + nums[right] + value > 0:
                    right -= 1
                else:
                    left += 1
        return res        