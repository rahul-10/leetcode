class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hash_map = {}

        for idx, val in enumerate(nums):
            if hash_map.get(val):
                return True
            hash_map[val] = True

        return False
        