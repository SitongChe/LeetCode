#https://leetcode.com/problems/zigzag-conversion/description/
#time O(n) space O(n)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ""
        diff = 2*numRows-2
        if diff == 0:
            return s
        for i in range(numRows):
            curDiff = diff-2*i
            for j in range(i,len(s),diff):
                ans+=s[j]
                if i!=0 and i!=numRows-1 and j+curDiff<len(s):
                    ans+=s[j+curDiff]
        return ans
            
