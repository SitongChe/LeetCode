#https://leetcode.com/problems/spiral-matrix/description/
#time O(n*m) space O(n*m)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = n-1
        up = 0
        down = m-1
        while left<=right and up<=down:
            for j in range(left,right+1):
                ans.append(matrix[up][j])
            up+=1
            if up>down:
                break
            for i in range(up,down+1):
                ans.append(matrix[i][right])
            right-=1
            if left>right:
                break
            for j in range(right,left-1,-1):
                ans.append(matrix[down][j])
            down-=1
            if up>down:
                break
            for i in range(down,up-1,-1):
                ans.append(matrix[i][left])
            left+=1
            if left>right:
                break
        return ans
        
        
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m = len(matrix)
        n = len(matrix[0])
        x=0
        y=0
        dirs=[[0,1],[1,0],[0,-1],[-1,0]]
        dirIndex = 0
        for _ in range(m*n):
            ans.append(matrix[x][y])
            matrix[x][y]=101
            dirx,diry=dirs[dirIndex]
            x+=dirx
            y+=diry
            if x<0 or x>=m or y<0 or y>=n or matrix[x][y]==101:
                x-=dirx
                y-=diry
                dirIndex=(1+dirIndex)%4
                dirx,diry=dirs[dirIndex]
                x+=dirx
                y+=diry
        return ans
            
        
