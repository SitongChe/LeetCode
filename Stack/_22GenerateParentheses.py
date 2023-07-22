#https://leetcode.com/problems/generate-parentheses/
#time O(C(n)) space O(N)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def traceback(left,right,tmp):
            if left == n and right == n:
                ans.append(tmp)
                return
            if left<n:
                traceback(left+1,right,tmp+"(")
            if left>right:
                traceback(left,right+1,tmp+")")
        ans = []
        traceback(0,0,"")
        return ans
