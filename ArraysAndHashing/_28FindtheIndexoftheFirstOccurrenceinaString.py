#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
#time O(m+n),space O(m)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lps = [0]*len(needle)
        i = 1
        p = 0
        while i < len(needle):
            if needle[i]==needle[p]:
                lps[i]=p+1
                i+=1
                p+=1
            else:
                if p == 0:
                    lps[i]=0
                    i+=1
                else:
                    p = lps[p-1]
        
        i = 0
        j = 0
        while i < len(haystack):
            if needle[j]==haystack[i]:
                i+=1
                j+=1
            else:
                if j == 0:
                    i+=1
                else:
                    j = lps[j-1]
            if j==len(needle):
                return i-len(needle)
        return -1





            
