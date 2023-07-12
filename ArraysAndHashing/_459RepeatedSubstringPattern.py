#https://leetcode.com/problems/repeated-substring-pattern/description/
#time O(n) ,space  O(n)
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        lps = [0]*len(s)
        p = 0
        i = 1
        while i < len(s):
            if s[i]==s[p]:
                lps[i]=p+1
                i+=1
                p+=1
            else:
                if p == 0:
                    lps[i]=0
                    i+=1
                else:
                    p = lps[p-1]
        return lps[-1] and lps[-1]%(len(s)-lps[-1])==0
