#https://leetcode.com/problems/string-matching-in-an-array/description/
#time O(n^2) ,space  O(n)
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        def kmp(s,sz):
            lsp=[0]*len(s)
            p = 0
            i = 1
            while i < len(s):
                if s[i]==s[p]:
                    lsp[i]=p+1
                    if lsp[i]==sz:
                        return True
                    i+=1
                    p+=1
                else:
                    if p == 0:
                        lsp[i]=0
                        i+=1
                    else:
                        p = lsp[p-1]
                
            return False
        words.sort(key = len)
        ans = []
        for i in range(len(words)):
            sz = len(words[i])
            s = '#'.join(words[i:])
            if kmp(s,sz):
                ans.append(words[i])
        return ans
  
# time O(n^2) space O(n)
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        s = '#'.join(words)
        return [i for i in words if s.count(i)>=2]
