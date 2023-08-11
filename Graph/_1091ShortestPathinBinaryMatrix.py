#https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
#time O(m*n) space O(m*n)
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def bfs(i,j):
            queue = [[i,j]]
            visited.add((i,j))
            ans = 1
            while queue:
                size = len(queue)
                for _ in range(size):
                    curi, curj = queue.pop(0)
                    if curi == m-1 and curj == n-1:
                        return ans
                    for diri,dirj in dirs:
                        i=curi+diri
                        j=curj+dirj
                        if i<0 or i>=m or j<0 or j>=n or (i,j) in visited or grid[i][j]==1:
                            continue
                        visited.add((i,j))
                        queue.append([i,j])
                ans+=1
            return -1
        m = len(grid)
        n = len(grid[0])
        dirs = [[1,0],[-1,0],[0,-1],[0,1],[1,1],[1,-1],[-1,1],[-1,-1]]
        visited = set()
        if grid[0][0]==1:
            return -1
        return bfs(0,0)
                        
