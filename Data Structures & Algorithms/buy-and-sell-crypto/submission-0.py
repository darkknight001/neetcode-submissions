class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lastPrice = prices[0]
        profit = 0
        currProfit = 0
        for i in range(1, len(prices)):
            currPrice = prices[i]
            if currPrice<=lastPrice:
                lastPrice = currPrice
                currProfit = 0 
            else:
                currProfit = currPrice-lastPrice
                profit = max(currProfit, profit)
        
        return profit

