class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for idx, val in enumerate(strs):
            sorted_val = "".join(sorted(val))
            if sorted_val not in res:
                res[sorted_val] = []
            res[sorted_val].append(val)
        
        return list(res.values())