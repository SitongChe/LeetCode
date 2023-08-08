#https://leetcode.com/problems/rotting-oranges/
#time O(M * N) space O(M * N)
#dfs
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = []
        freshCount = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append([i,j])
                elif grid[i][j]==1:
                    freshCount += 1
        if freshCount == 0:
            return 0
        if not queue:
            return -1
        time = 0
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        while queue and freshCount:
            size = len(queue)
            for _ in range(size):
                i,j = queue.pop(0)
                for diri,dirj in dirs:
                    ii = i+diri
                    jj = j+dirj
                    if ii<0 or ii>=m or jj<0 or jj>=n:
                        continue
                    if grid[ii][jj]==1:
                        grid[ii][jj]=2
                        freshCount-=1
                        queue.append([ii,jj])
            time +=1
        return time if freshCount == 0 else -1





