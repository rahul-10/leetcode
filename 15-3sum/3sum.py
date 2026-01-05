class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)-2):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums)-1
            while left < right:
                
                if nums[left] + nums[right] + nums[i] == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while left < len(nums) and nums[left] == nums[left-1]:
                        left += 1

                    while right >= 0 and nums[right] == nums[right+1]:
                        right -= 1

                elif nums[left] + nums[right] + nums[i] > 0:
                    right = right-1
                else:
                    left += 1
        return result


        