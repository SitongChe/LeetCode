#https://leetcode.com/problems/as-far-from-land-as-possible/description/
#time O(m * n) space O(m * n)
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        total = sum(sum(row) for row in grid)
        if total==0 or total==m*n:
            return -1
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    queue.append([i,j])
        def bfs():
            while queue:
                size = len(queue)
                for _ in range(size):
                    curi, curj = queue.pop(0)
                    for diri,dirj in dirs:
                        i = curi+diri
                        j = curj+dirj
                        if i<0 or i>=m or j<0 or j>=n or grid[i][j]!=0:
                            continue
                        grid[i][j]=1+grid[curi][curj]
                        queue.append([i,j])
        bfs()
        ans = -1
        for i in range(m):
            for j in range(n):
                ans = max(ans,grid[i][j]-1)
        return ans




        
