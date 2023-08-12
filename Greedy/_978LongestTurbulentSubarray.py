#https://leetcode.com/problems/longest-turbulent-subarray/description/
#time O(N) space O(1)
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l = 0
        r = 1
        prev = ""
        ans = 1
        while r < len(arr):
            if arr[r]>arr[r-1] and prev!=">":
                ans = max(ans,r-l+1)
                r+=1
                prev = ">"
            elif arr[r]<arr[r-1] and prev!="<":
                ans = max(ans,r-l+1)
                r+=1
                prev = "<"
            else:
                if arr[r]==arr[r-1]:
                    r+=1
                l = r-1
                prev = ""
        return ans





