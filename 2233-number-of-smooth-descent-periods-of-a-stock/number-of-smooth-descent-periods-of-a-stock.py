class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count = prev = 1
        for i in range(1, len(prices)):
            prev = prev + 1 if prices[i] + 1 == prices[i-1] else 1
            count += prev
        
        return count

