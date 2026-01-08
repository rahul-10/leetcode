from functools import cmp_to_key

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        def sorting_logic(a, b):
            a = a.split(" ")
            b = b.split(" ")
            i = 1
            while True:
                x = ""
                if i < len(a):
                    x = a[i]
                
                y = ""
                if i < len(b):
                    y = b[i]
                
                if not x and not y:
                    return -1 if a[0]<b[0] else 1

                if x.isdigit() and y.isdigit():
                    return 0

                if not x or (not x.isdigit() and y.isdigit()):
                    return -1
                
                if not y or (x.isdigit() and not y.isdigit()):
                    return 1
                
                if x < y:
                    return -1
                if x > y:
                    return 1
                
                i += 1
            
        logs.sort(key=cmp_to_key(sorting_logic))
        
        return logs
            
        
