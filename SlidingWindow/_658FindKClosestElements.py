#https://leetcode.com/problems/find-k-closest-elements/description/
#time O(log(n-k)), space O(k)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr)-k-1
        while left+1 <right:
            mid = left + (right-left)//2
            if x>(arr[mid]+arr[mid+k])/2:
                left = mid
            else:
                right = mid
        if right+k < len(arr) and x>(arr[right]+arr[right+k])/2:
            return arr[right+1:right+1+k]
        if left+k < len(arr) and x>(arr[left]+arr[left+k])/2:
            return arr[right:right+k]
        return arr[left:left+k]

#time O(logN), space O(k)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr)-1
        idx = 0
        val = arr[0]
        while l+1<r:
            mid = l+(r-l)//2
            curDiff = abs(arr[mid]-x)
            resDiff = abs(val-x)
            if curDiff<resDiff or (curDiff == resDiff and arr[mid]<val):
                val = arr[mid]
                idx = mid
            if arr[mid]==x:
                break
            elif arr[mid]<x:
                l=mid
            else:
                r=mid
        l = r = idx
        for i in range(k-1):
            if l == 0:
                r+=1
            elif r==len(arr)-1 or x-arr[l-1]<=arr[r+1]-x:
                l-=1
            else:
                r+=1
        return arr[l:r+1]
