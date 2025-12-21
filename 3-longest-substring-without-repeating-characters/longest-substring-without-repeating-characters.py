class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start_index = 0
        hash_map = {}
        max_length = 0

        for idx, val in enumerate(s):
            hashed_val = hash_map.get(val, None)
            if hashed_val is not None and hashed_val >= start_index :
                start_index = hash_map.get(val) + 1
            
            hash_map[val] = idx
            max_length = max (max_length, idx - start_index + 1)

        return max_length



        
            
        