import sys

class Solution:
    def find_min(self, map:dict) -> int:   
        max_value = 0
        key_wiyh_hightest_count = None
        total_count = 0
        for key, value in map.items():
            if value == 0:
                continue
            total_count = total_count + value
            if max_value < value:
                max_value = value
                key_wiyh_hightest_count = key
       
        return  total_count - map[key_wiyh_hightest_count]

    def characterReplacement(self, s: str, k: int) -> int:
        max_count = 0
        replaced = 0
        map = {}
        starting_index = 0
        for index in range(0, len(s)):
            map[s[index]] = map.get(s[index], 0) + 1
            while self.find_min(map) > k:
                map[s[starting_index]] = map.get(s[starting_index], 0) - 1
                starting_index = starting_index + 1
                
            if max_count < index - starting_index + 1:
                max_count = index - starting_index + 1
                

        return max_count

            
        