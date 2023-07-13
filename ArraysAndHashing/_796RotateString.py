#https://leetcode.com/problems/rotate-string/description/
#time O(n) ,space  O(n)
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        n= len(s)
        lsp=[0]*n
        p = 0
        i = 1
        while i<n:
            if goal[i]==goal[p]:
                lsp[i]=p+1
                p+=1
                i+=1
            else:
                if p==0:
                    lsp[i]=0
                    i+=1
                else:
                    p = lsp[p-1]
        
        i = 0
        j = 0
        while i < n:
            if s[(i+j)%n]==goal[j]:
                j+=1
            else:
                if j == 0:
                    i+=1
                else:
                    i += j-lsp[j-1]
                    j = lsp[j-1]
            if j == n:
                return True
        return False
                    
