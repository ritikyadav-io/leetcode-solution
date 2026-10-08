class Solution(object):
    def maxProfit(self, prices):
        max_profit=0
        min_val=float("inf")
        n =len(prices)
        for i in range(0,n):
            min_val=min(min_val,prices[i])
            max_profit=max(max_profit,prices[i]-min_val)
        return max_profit
        