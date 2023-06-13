#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#time O(N), space O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        n = len(prices)
        if n == 0:
            return 0
        minPrice = prices[0]
        for price in prices:
            ans = max(ans, price-minPrice)
            minPrice = min(minPrice, price)
        return ans
