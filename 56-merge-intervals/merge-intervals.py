class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        res = [intervals[0]]
        for _, val in enumerate(intervals[1:]):
            if val[0] > res[-1][1]:
                res.append(val)
                continue
            
            res[-1][1] = max(res[-1][1], val[1])\

        return res


        