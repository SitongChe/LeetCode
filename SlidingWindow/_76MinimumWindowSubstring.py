#https://leetcode.com/problems/minimum-window-substring/
#time O(N), space O(k), where k is the size of the character set
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        k = len(t)
        start,end = 0,0
        ansS,ansE = -1,-1
        for end in range(len(s)):
            count[s[end]]-=1
            if count[s[end]]>=0:
                k-=1
            while k == 0:
                if ansS == -1 or ansE-ansS>end-start:
                    ansS = start
                    ansE = end
                if count[s[start]]==0:
                    k+=1
                count[s[start]]+=1
                start+=1
        if ansS == -1:
            return ""
        return s[ansS:ansE+1]


            
