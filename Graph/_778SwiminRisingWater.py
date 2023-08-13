#https://leetcode.com/problems/swim-in-rising-water/
#time O(NlogN) space O(N)
#priority queue
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minHeap = [[grid[0][0],0,0]]
        visited = set()
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        while minHeap:
            time,x,y = heapq.heappop(minHeap)
            if (x,y) not in visited:
                visited.add((x,y))
                if x==n-1 and y==n-1:
                    return time
                for diri,dirj in dirs:
                    xx = x+diri
                    yy = y+dirj
                    if xx<0 or xx>=n or yy<0 or yy>=n or (xx,yy) in visited:
                        continue
                    heapq.heappush(minHeap,[max(time,grid[xx][yy]),xx,yy])
        return 0
        
