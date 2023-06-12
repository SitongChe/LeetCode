#https://leetcode.com/problems/swim-in-rising-water/
#time O(NlogN) space O(N)
#priority queue
    def swimInWater(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)
        if n == 0:
            return 0
        minHeap = [[grid[0][0],0,0]]
        dirs=[[0,1],[0,-1],[1,0],[-1,0]]
        visited = set()
        while minHeap:
            time,x,y = heapq.heappop(minHeap)
            if (x,y) in visited:
                continue
            ans = max(ans,time)
            if x==n-1 and y==n-1:
                return ans
            visited.add((x,y))
            for dirx,diry in dirs:
                xx = x+dirx
                yy = y+diry
                if xx>=0 and xx<n and yy>=0 and yy<n and (xx,yy) not in visited:
                    heapq.heappush(minHeap,[grid[xx][yy],xx,yy])
        return ans

