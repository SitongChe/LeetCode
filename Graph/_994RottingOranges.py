#https://leetcode.com/problems/rotting-oranges/
#time O(M * N) space O(M * N)
#dfs
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = []
        freshOrangeCount = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append((i,j))
                elif grid[i][j]==1:
                    freshOrangeCount += 1
        if freshOrangeCount == 0:
            return 0
        if not queue:
            return -1
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        time = 0
        while queue:
            size = len(queue)
            for i in range(size):
                x,y = queue.pop(0)
                for dx, dy in dirs:
                    newX = x+dx
                    newY = y+dy
                    if newX<0 or newX>=m or newY<0 or newY>=n:
                        continue
                    if grid[newX][newY]==1:
                        grid[newX][newY]=2
                        queue.append((newX,newY))
                        freshOrangeCount-=1
            time += 1
        if freshOrangeCount == 0:
            return time-1
        return -1







