#https://leetcode.com/problems/repeated-string-match/description/
#time O(n) ,space  O(n)
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        lps = [0]*len(b)
        p = 0
        i = 1
        while i < len(b):
            if b[i]==b[p]:
                lps[i]=p+1
                p+=1
                i+=1
            else:
                if p == 0:
                    lps[i]=0
                    i+=1
                else:
                    p = lps[p-1]
        
        i = 0
        j = 0
        while i<len(a):
            if a[(i+j)%(len(a))]==b[j]:
                j+=1
            else:
                if j == 0:
                    i+=1
                else:
                    i+=(j-lps[j-1])
                    j = lps[j-1]
            if j == len(b):
                return (i+j-1)//(len(a))+1
        return -1
            
