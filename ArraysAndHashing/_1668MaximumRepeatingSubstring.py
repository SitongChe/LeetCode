#https://leetcode.com/problems/maximum-repeating-substring/description/
#time O(n) ,space  O(n)
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(word)
        maxRepeat = len(sequence)//n
        lsp = [0]*(maxRepeat*n+1)
        p = 0
        i = 1
        repeatedWord = word*maxRepeat+'$'
        while i<len(repeatedWord):
            if repeatedWord[i]==repeatedWord[p]:
                lsp[i]=p+1
                p+=1
                i+=1
            else:
                if p == 0:
                    lsp[i]=0
                    i+=1
                else:
                    p=lsp[p-1]
        
        i = 0
        j = 0
        ans = 0
        while i<len(sequence):
            if sequence[i]==repeatedWord[j]:
                i+=1
                j+=1
            else:
                if j == 0:
                    i+=1
                else:
                    j = lsp[j-1]
            ans = max(ans,j//n)
        return ans
