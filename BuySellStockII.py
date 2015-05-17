#Say you have an array for which the ith element is the price of a given stock on day i.

#Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if (len(prices) <=1):
            return 0
        i = 0
        profit = 0
        n = len(prices)
        while(i<n-1):
            # local minima
            while(i<n-1 and prices[i+1]<=prices[i]):
                i=i+1
            if i == n-1:
                break
            local_min = prices[i]
            i = i+1            
            while(i<n and prices[i]>=prices[i-1]):
                i = i+1
            local_max = prices[i-1]
            profit+=(local_max - local_min)
        return profit
s = Solution()
print s.maxProfit([1,2])