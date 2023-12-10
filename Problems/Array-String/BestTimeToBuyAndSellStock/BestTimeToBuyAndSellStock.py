# create folders with a file for code and a file for description

def maxProfit(self, prices):
        maxProfit = 0
        min_price = prices[0]

        for price in prices:
            if price < min_price :
                min_price = price
            else :
                maxProfit = max(maxProfit, price - min_price)
        return maxProfit