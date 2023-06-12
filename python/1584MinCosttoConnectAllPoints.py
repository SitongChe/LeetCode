#https://leetcode.com/problems/min-cost-to-connect-all-points/
#time O(NlogN) space O(N)
#priority queue
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        minHeap = [[0,points[0][0],points[0][1]]]
        ans = 0
        visited = set()
        while minHeap:
            dist,x,y = heapq.heappop(minHeap)
            if (x,y) in visited:
                continue
            ans += dist
            visited.add((x,y))
            for xx,yy in points:
                if (xx,yy) not in visited:
                    val = abs(xx-x)+abs(yy-y)
                    heapq.heappush(minHeap,[val,xx,yy])
        return ans




