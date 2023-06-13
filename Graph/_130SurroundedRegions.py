#https://leetcode.com/problems/surrounded-regions/
#time O(M * N * α(M * N)) space O(M * N)
#union find
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        uf = {}
        def find(x):
            uf.setdefault(x,x)
            if x!=uf[x]:
                uf[x]= find(uf[x])
            return uf[x]
        def union(x,y):
            rootx = find(x)
            rooty = find(y)
            uf[rootx]=rooty
        for i in range(m):
            if board[i][0]=="O":
                union((i,0),(m,n))
            if board[i][n-1]=="O":
                union((i,n-1),(m,n))
        for j in range(n):
            if board[0][j]=="O":
                union((0,j),(m,n))
            if board[m-1][j]=="O":
                union((m-1,j),(m,n))
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O":
                    if i>0 and board[i-1][j]=="O":
                        union((i-1,j),(i,j))
                    if j>0 and board[i][j-1]=="O":
                        union((i,j-1),(i,j))
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O":
                    if find((i,j))!=find((m,n)):
                        board[i][j]="X"

#time O(M * N) space O(M * N)
#dfs
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        visited = [[False]*n for i in range(m)]
        def dfs(i,j):
            if i <0 or i>=m or j<0 or j>=n or board[i][j]!="O" or visited[i][j]:
                return
            visited[i][j]=True
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        for j in range(n):
            dfs(0,j)
            dfs(m-1,j)
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O" and not visited[i][j]:
                    board[i][j]="X"
        
                    



