class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 101
        max_profit = 0
        for price in prices:
            min_price = min(price,min_price)
            max_profit = max((price - min_price),max_profit)
        return max_profit

