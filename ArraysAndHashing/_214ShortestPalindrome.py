#https://leetcode.com/problems/shortest-palindrome/description/
#time O(n) ,space  O(n)
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        l = s + "#" + s[::-1]
        lsp = [0]*len(l)
        i = 1
        p = 0
        while i<len(l):
            if l[i]==l[p]:
                lsp[i]=p+1
                i+=1
                p+=1
            else:
                if p == 0:
                    lsp[i]=0
                    i+=1
                else:
                    p = lsp[p-1]
        r = s[lsp[-1]:]
        return r[::-1]+s
