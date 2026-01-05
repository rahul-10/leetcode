class Solution:
    def can_append(self, x, y, z, result_map) -> bool:
        nums = [x, y, z]
        nums.sort()
        
        if result_map.get(nums[0], None) is None:
            result_map[nums[0]] = {}

        if result_map.get(nums[0]).get(nums[1]) == nums[2]:
            return False

        
        result_map[nums[0]][nums[1]] = nums[2]
        return True
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        result_map = {}
        nums.sort()
        is_processed = {}
        for i in range(len(nums)):
            if is_processed.get(i, None) is None:
                is_processed[i]= {} 

            if i >= 1 and nums[i] == nums[i-1]:
                continue
            hash_map = {}
            for j in range(i+1, len(nums)):
                if is_processed[i].get(j, None) == True:
                    continue
                k = -1 * (nums[i] + nums[j]) 
                if k in hash_map and self.can_append(nums[i], nums[j], k, result_map):
                    is_processed[i][j] = True
                    result.append([nums[i], nums[j], k])
                
                hash_map[nums[j]] = j
        
        return result


        