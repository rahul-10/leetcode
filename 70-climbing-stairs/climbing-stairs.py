class Solution:
    def climbStairs(self, n: int) -> int:
        x = 0
        y = 1
        for  index in range(1, n+1):
            temp = x+y
            x = y 
            y = temp
        return y
    
    