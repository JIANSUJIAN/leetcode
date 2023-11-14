#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
## 1
## Array
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        buy_price = prices[0]
        profit = 0

        for i in range(1, n):
            if prices[i] < buy_price:
                buy_price = prices[i]
            else:
                profit = max(prices[i] - buy_price, profit)
        return profit
        
## 2 
## DP
# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:

        
# @lc code=end

