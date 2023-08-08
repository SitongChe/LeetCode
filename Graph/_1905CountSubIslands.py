#https://leetcode.com/problems/count-sub-islands/description/
#time O(m*n) space O(m*n)
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid2[i][j]==0 or (i,j) in visited:
                return True
            if grid1[i][j]==0:
                return False
            visited.add((i,j))
            # cannot do dfs(i+1,j) and dfs(i-1,j) and dfs(i,j+1) and dfs(i,j-1), since the rest of the dfs won't run if the first is set to false
            # also cannot do ans = ans and dfs(i-1,j)
            ans = True
            ans = dfs(i+1,j) and ans
            ans = dfs(i-1,j) and ans
            ans = dfs(i,j+1) and ans
            ans = dfs(i,j-1) and ans
            return ans
            
        m = len(grid2)
        n = len(grid2[0])
        ans = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid2[i][j]==1 and (i,j) not in visited:
                    if dfs(i,j):
                        ans+=1
        return ans
        
