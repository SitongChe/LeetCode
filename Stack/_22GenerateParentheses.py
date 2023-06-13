#https://leetcode.com/problems/generate-parentheses/
#time O(C(n)) space O(N)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        ans = []
        def traceback(openN,closedN):
            if openN == closedN == n:
                ans.append("".join(stack))
                return
            if openN<n:
                stack.append("(")
                traceback(openN+1,closedN)
                stack.pop()
            if closedN<openN:
                stack.append(")")
                traceback(openN,closedN+1)
                stack.pop()
        traceback(0,0)
        return ans
