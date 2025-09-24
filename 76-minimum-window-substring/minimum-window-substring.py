class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = len(t)

        target_map = {}
        for idx, char in enumerate(t):
            target_map[char] = target_map.get(char, 0) + 1

        source_map = {}
        j = 0
        
        final_substring = ""

        for i, char in enumerate(s):
            while counter >0 and  j < len(s):
                source_map[s[j]] = source_map.get(s[j], 0) + 1
                if source_map[s[j]] <= target_map.get(s[j], 0):
                    counter -= 1
                j += 1
            if counter == 0 and (not final_substring or len(final_substring) > len(s[i:j-1])):
                final_substring = s[i:j]
            
            if source_map[char] <= target_map.get(char, 0):
                counter += 1
            source_map[char] = source_map[char] -1
        return final_substring


