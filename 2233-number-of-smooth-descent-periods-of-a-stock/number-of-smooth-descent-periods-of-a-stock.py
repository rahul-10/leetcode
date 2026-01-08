class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count = prev = 1
        for idx, val in enumerate(prices[1:], start=1):
            prev = prev + 1 if val + 1 == prices[idx-1] else 1
            count += prev
        
        return count

