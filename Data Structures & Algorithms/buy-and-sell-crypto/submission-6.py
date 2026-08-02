class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if len(prices) == 0:
            return max_profit
        lowest = prices[0]
        for price in prices:
            curr_profit = price - lowest
            if curr_profit > max_profit:
                max_profit = curr_profit
            if price < lowest:
                lowest = price
        return max_profit
        