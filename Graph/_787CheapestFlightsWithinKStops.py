#https://leetcode.com/problems/cheapest-flights-within-k-stops/
#time O(N^k) space O(N)
#dijistra
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [inf]*n
        prices[src]=0
        for i in range(k+1):
            tmpPrices = prices.copy()
            for u,v,c in flights:
                if prices[u]==inf:
                    continue
                if prices[u]+c<tmpPrices[v]:
                    tmpPrices[v]=prices[u]+c
            prices = tmpPrices
        return prices[dst] if prices[dst]!=inf else -1

