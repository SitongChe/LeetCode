#https://leetcode.com/problems/swim-in-rising-water/
#time O(NlogN) space O(N)
#priority queue
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        heap = [[grid[0][0],0,0]]
        ans = 0
        while heap:
            time, x, y = heapq.heappop(heap)
            if (x,y) in visited:
                continue
            ans = max(ans,time)
            if x == n-1 and y == n-1:
                return ans
            visited.add((x,y))
            for nx,ny in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                if nx>=0 and nx<n and ny>=0 and ny<n and (nx,ny) not in visited:
                    heapq.heappush(heap,[grid[nx][ny],nx,ny])
        return ans

