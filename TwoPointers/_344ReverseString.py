#https://leetcode.com/problems/merge-sorted-array/description/
#time O(n), space O(1)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s)-1
        while l<r:
            s[r],s[l]=s[l],s[r]
            l+=1
            r-=1
        
