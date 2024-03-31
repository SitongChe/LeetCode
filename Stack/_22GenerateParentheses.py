#https://leetcode.com/problems/generate-parentheses/
#time O(C(n)) space O(N)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def traceback(left,right,tmp):
            if left==0 and right==0:
                ans.append(tmp)
                return
            if left>0:
                traceback(left-1,right,tmp+"(")
            if right>left:
                traceback(left,right-1,tmp+")")
        ans = []
        traceback(n,n,"")
        return ans
