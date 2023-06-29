#https://leetcode.com/problems/min-cost-to-connect-all-points/
#time O(NlogN) space O(N)
#priority queue
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        heap = [[0,points[0][0],points[0][1]]]
        visited = set()
        ans = 0
        while heap:
            dis,u,v = heapq.heappop(heap)
            if (u,v) not in visited:
                ans += dis
                visited.add((u,v))
                for i,j in points:
                    if (i,j) not in visited:
                        val = abs(i-u)+abs(j-v)
                        heapq.heappush(heap,[val,i,j])
        return ans





