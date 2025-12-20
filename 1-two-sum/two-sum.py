class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash_map = {}

        for idx, val in enumerate(nums):
            if not hash_map.get(val):
                hash_map[val] = []
            hash_map[val].append(idx)


        nums.sort()

        left = 0
        right=len(nums)-1
        result = []
        while(left < right):
            if nums[left] + nums[right] < target:
                left += 1
                continue
            if nums[left] + nums[right] > target:
                right -= 1
                continue
            x = hash_map[nums[left]][0]
            hash_map[nums[left]].pop(0)
            y = hash_map[nums[right]][0]
            result = [x, y]
            break

        return result