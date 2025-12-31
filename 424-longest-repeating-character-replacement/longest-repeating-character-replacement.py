class Solution:
    def get_max_freq(self, hash_map: dict) -> int:
        freq = 0

        for val in hash_map.values():
            freq = max(freq, val)
        
        return freq
        
    def characterReplacement(self, s: str, k: int) -> int:

        longest_len = 0
        start = 0
        max_freq = 0
        hash_map = {}

        for idx, val in enumerate(s): 
            window_size = idx - start +1 
            
            hash_map[val] = hash_map.get(val, 0) + 1
            max_freq = max(max_freq, hash_map[val])

            if window_size - max_freq <= k: 
                longest_len = max(longest_len, window_size)
            else:
                while window_size - max_freq > k:
                    hash_map[s[start]] = hash_map[s[start]] - 1
                    start += 1
                    # max_freq = self.get_max_freq(hash_map)
                    window_size = idx - start +1 

        return longest_len    