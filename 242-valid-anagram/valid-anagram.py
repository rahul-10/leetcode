class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for c in s:
            map[c] = map.get(c, 0) + 1
        
        for c in t:
            if not map.get(c, 0):
                return False
            map[c] = map.get(c) - 1

        for key, value in map.items():
            if value != 0:
                return False
        return True
        

        