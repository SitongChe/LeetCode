#https://leetcode.com/problems/shortest-bridge/description/
#time O(m*n) space O(m*n)
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0 or (i,j) in visited:
                return
            visited.add((i,j))
            for diri,dirj in dirs:
                dfs(i+diri,j+dirj)
        def bfs():
            ans = 0
            queue = deque(visited)
            while queue:
                size = len(queue)
                for _ in range(size):
                    curi,curj = queue.popleft()
                    for diri,dirj in dirs:
                        i = curi+diri
                        j = curj+dirj
                        if i<0 or i>=m or j<0 or j>=n or (i,j) in visited:
                            continue
                        if grid[i][j]:
                            return ans
                        queue.append((i,j))
                        visited.add((i,j))
                ans+=1
            return ans
        m = len(grid)
        n = len(grid[0])
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    dfs(i,j)
                    return bfs()
