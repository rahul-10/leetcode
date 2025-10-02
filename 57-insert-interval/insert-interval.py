class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        res:List[List[int]]  = []
        i =0
        new_interval_added = False
        while i < len(intervals):
            if intervals[i][1] < newInterval[0] or new_interval_added:
                res.append(intervals[i])
                i = i+1
                continue
            if intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                new_interval_added = True
                continue
            start_value = min(intervals[i][0], newInterval[0])
            end_value = max(intervals[i][1], newInterval[1])
            j = i+1
            while j<len(intervals) and end_value >= intervals[j][0]:
                end_value = max(end_value, intervals[j][1])
                j = j+1
                
            res.append([start_value, end_value])
            i = j
            new_interval_added = True
        if not new_interval_added:
            res.append(newInterval)
        return res

        