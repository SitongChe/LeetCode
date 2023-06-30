#https://leetcode.com/problems/path-with-minimum-effort/description/
#time O(m * n * log(m * n)) space O(m * n)
#priority queue
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        visited = set()
        ans = 0
        heap = [(0,0,0)]
        while heap:
            d,x,y = heapq.heappop(heap)
            if (x,y) in visited:
                continue
            ans = max(ans,d)
            if (x,y)==(m-1,n-1):
                return ans
            visited.add((x,y))
            for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                if nx>=0 and nx<m and ny>=0 and ny<n and (nx,ny) not in visited:
                    newDist = abs(heights[nx][ny]-heights[x][y])
                    heapq.heappush(heap,(newDist,nx,ny))
        return ans


