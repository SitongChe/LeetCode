#https://leetcode.com/problems/longest-happy-prefix/description/
#time O(n) ,space  O(n)
class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        lsp = [0]*n
        p = 0
        i = 1
        while i < n:
            if s[i]==s[p]:
                lsp[i]=p+1
                i+=1
                p+=1
            else:
                if p == 0:
                    lsp[i]=0
                    i+=1
                else:
                    p = lsp[p-1]
        return s[:lsp[-1]]
