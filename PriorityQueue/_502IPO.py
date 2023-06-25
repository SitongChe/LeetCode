#https://leetcode.com/problems/ipo/description/
#time O(n log n) space O(N)
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        proj = [[c,p] for c,p in zip(capital,profits)]
        heapq.heapify(proj)
        maxHeap = []
        for i in range(k):
            while proj and proj[0][0]<=w:
                c,p = heapq.heappop(proj)
                heapq.heappush(maxHeap,-p)
            if not maxHeap:
                return w
            w -= heapq.heappop(maxHeap)
        return w

