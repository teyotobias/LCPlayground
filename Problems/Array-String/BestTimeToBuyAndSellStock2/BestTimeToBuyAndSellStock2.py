
# 11/10/2023 02:13	Accepted	49 ms	17.7 MB	python3

def maxProfit(self, prices):
        maxProfit = 0
        for i in range(len(prices)-1):
            growth = prices[i+1] - prices[i]
            maxProfit = max(maxProfit, maxProfit + growth)
        return maxProfit