#https://leetcode.com/problems/count-sub-islands/description/
#time O(m*n) space O(m*n)
#priority queue
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or (i,j) in visited or grid2[i][j]==0:
                return True
            visited.add((i,j))
            res = True
            if grid1[i][j]==0:
                res = False
            res = dfs(i+1,j) and res
            res = dfs(i-1,j) and res
            res = dfs(i,j+1) and res
            res = dfs(i,j-1) and res
            return res
        m = len(grid1)
        n = len(grid1[0])
        ans = 0
        visited=set()
        for i in range(m):
            for j in range(n):
                if grid2[i][j]==1 and (i,j) not in visited and dfs(i,j):
                    ans += 1
        return ans
            
