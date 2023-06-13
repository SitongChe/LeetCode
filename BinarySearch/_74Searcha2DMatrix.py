#https://leetcode.com/problems/search-a-2d-matrix/
#time O(log M + log N), space O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        rowl = 0
        rowr = m-1
        row = 0
        while rowl+1<rowr:
            mid = rowl + (rowr-rowl)//2
            if matrix[mid][0]<target:
                rowl = mid
            else:
                rowr = mid
        if matrix[rowr][0]<=target:
            row=rowr
        elif matrix[rowl][0]<=target:
            row=rowl
        else:
            return False
        
        coll = 0
        colr = n-1
        col = 0
        while coll+1<colr:
            mid = coll+(colr-coll)//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]<target:
                coll = mid
            else:
                colr = mid
        if matrix[row][coll]==target or matrix[row][colr]==target:
            return True
        return False
        
