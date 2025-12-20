import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_return = 0
        min_price = max_price = sys.maxsize
    

        for idx, price in enumerate(prices):
            if price < min_price:
                min_price = max_price = price
                continue
            elif price > max_price:
                max_price = price
                max_return = max(max_price-min_price, max_return)

        return max_return

            

