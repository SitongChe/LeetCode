#https://leetcode.com/problems/cheapest-flights-within-k-stops/
#time O(k*E) space O(n)
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

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(dict)
        for a,b,p in flights:
            graph[a][b]=p
        heap = [[0,src,k+1]]
        while heap:
            p,i,k = heapq.heappop(heap)
            if i == dst:
                return p
            if k>0:
                for j in graph[i]:
                    heapq.heappush(heap,[p+graph[i][j],j,k-1])
        return -1
