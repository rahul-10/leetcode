class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        while i < len(intervals):
            # Just add current interval if new interval is out its range
            if newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
                i += 1
                continue
            
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
            else:
                min_val = min(newInterval[0],  intervals[i][0])
                max_val = max(newInterval[1],  intervals[i][1])
                i += 1
                while i < len(intervals) and intervals[i][0] <= max_val:
                    max_val = max(max_val, intervals[i][1])
                    i += 1
                
                result.append([min_val, max_val])
            result.extend(intervals[i:])
            return result
        
        result.append(newInterval)
        return result