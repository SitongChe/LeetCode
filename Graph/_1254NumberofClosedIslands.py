#https://leetcode.com/problems/number-of-closed-islands/description/
#time O(V + E) space O(V + E) 
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==1 or (i,j) in visited:
                return
            visited.add((i,j))
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        m = len(grid)
        n = len(grid[0])
        visited = set()
        for i in range(m):
            if grid[i][0]==0:
                dfs(i,0)
            if grid[i][n-1]==0:
                dfs(i,n-1)
        for j in range(n):
            if grid[0][j]==0:
                dfs(0,j)
            if grid[m-1][j]==0:
                dfs(m-1,j)
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0 and (i,j) not in visited:
                    ans+=1
                    dfs(i,j)
        return ans


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n:
                return 0
            if grid[i][j]==1 or (i,j) in visited:
                return 1
            visited.add((i,j))
            return min(dfs(i+1,j),dfs(i-1,j),dfs(i,j+1),dfs(i,j-1))

        m = len(grid)
        n = len(grid[0])
        visited = set()
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0 and (i,j) not in visited:
                    if dfs(i,j):
                        ans+=1
        return ans




        
