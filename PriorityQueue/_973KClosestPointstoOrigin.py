#https://leetcode.com/problems/k-closest-points-to-origin/
#time O(N+klogN) space O(N)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        ans = []
        for x,y in points:
            minHeap.append([x*x+y*y,x,y])
        heapq.heapify(minHeap)
        for i in range(k):
            dist,x,y = heapq.heappop(minHeap)
            ans.append([x,y])
        return ans
        
