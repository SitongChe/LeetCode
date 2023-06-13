#https://leetcode.com/problems/number-of-islands/
#time O(N*M) space O(N*M)
#bfs dfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        def dfs(i,j,visited):
            if i<0 or i>=m or j<0 or j>=n or (i,j) in visited or grid[i][j]=="0":
                return
            visited.add((i,j))
            dfs(i+1,j,visited)
            dfs(i-1,j,visited)
            dfs(i,j+1,visited)
            dfs(i,j-1,visited)
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        def bfs(i,j,visited):
            visited.add((i,j))
            queue = [(i,j)]
            while queue:
                i,j = queue.pop(0)
                for dir in dirs:
                    ii = i+dir[0]
                    jj = j+dir[1]
                    if ii<0 or ii>=m or jj<0 or jj>=n or (ii,jj) in visited or grid[ii][jj]=="0":
                        continue
                    visited.add((ii,jj))
                    queue.append((ii,jj))


        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and (i,j) not in visited:
                    ans+=1
                    bfs(i,j,visited)
        return ans
                    



