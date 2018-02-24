class Solution:
    def maxProfit(self, prices):
        if len(prices) < 2: return 0
        buy, sale, profit = prices[0],0,0
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] > buy:
                sale = prices[i]
                if sale - buy > profit:
                    profit = sale - buy
        if sale == 0: return 0
        return profit
        