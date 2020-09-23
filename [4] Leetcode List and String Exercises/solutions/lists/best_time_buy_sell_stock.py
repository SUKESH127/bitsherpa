class Solution:

    #QUESTION: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/

    #APPROACH: We essentially want to iterate through the stock price array, while
    # keeping track of the minimum observed price. For the ith element in prices (ie ith time interval/stock price)
    # the max possible profit at time i (curMaxProfit) equals prices[i] minus minimum observed price from all previous times.
    # The global maxProfit will be the max profit across all the time intervals (ie i from 0 to len(prices)), so 
    # we keep track of this globalMax while iterating through the prices array.
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        globalMaxProfit, curMaxProfit = 0,0
        
        #This will keep track of the minimum price observed in the array
        minPrice = prices[0]
        
        
        for p in prices[1:]:
            #compute the maximum profit if we sold at the current price
            curMaxProfit = p - minPrice

            #update global max profit if necessary
            globalMaxProfit = max(globalMaxProfit,curMaxProfit)
            
            #update minimum price if necessary
            minPrice = min(p, minPrice)
        return globalMaxProfit