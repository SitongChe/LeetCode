#https://leetcode.com/problems/letter-combinations-of-a-phone-number/
#time O(4^N) space O(N*4^N)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map  = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        n = len(digits)
        if n == 0:
            return []
        ans = []
        def traceback(tmp,index):
            if len(tmp)==n:
                ans.append(tmp)
                return
            cur = map[digits[index]]
            for j in range(len(cur)):
                traceback(tmp+cur[j],index+1)
        traceback("",0)
        return ans

                    



