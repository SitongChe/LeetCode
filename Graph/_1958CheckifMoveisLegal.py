#https://leetcode.com/problems/check-if-move-is-legal/description/
#time O(m*n*8) space O(min(m,n))
class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        def dfs(i,j,diri,dirj,length,color):
            i = i+diri
            j = j+dirj
            if i<0 or i>=m or j<0 or j>=n or board[i][j]=='.':
                return False
            length+=1
            if board[i][j]==color:
                if length>=3:
                    return True
                return False
            return dfs(i,j,diri,dirj,length,color)
        m = len(board)
        n = len(board[0])
        dirs = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
        for diri,dirj in dirs:
            if dfs(rMove,cMove,diri,dirj,1,color):
                return True
        return False



