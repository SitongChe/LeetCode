#https://leetcode.com/problems/letter-combinations-of-a-phone-number/
#time O(4^N) space O(N*4^N)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def traceback(i,tmp):
            if i == n:
                if tmp:
                    ans.append(tmp)
                return
            for c in mapping[digits[i]]:
                traceback(i+1,tmp+c)
        n = len(digits)
        mapping = {"1":"","2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"qprs","8":"tuv","9":"wxyz"}
        ans = []
        traceback(0,"")
        return ans        
                    



