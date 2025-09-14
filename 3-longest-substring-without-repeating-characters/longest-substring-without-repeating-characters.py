class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}

        starting_index=0
        max_length = 0
        for index in range(0, len(s)):
            if s[index] in map and map[s[index]] >= starting_index:
                starting_index = map[s[index]] + 1
            map[s[index]] = index
            if (index - starting_index + 1) > max_length:
                max_length = index - starting_index + 1

        return max_length
            
        