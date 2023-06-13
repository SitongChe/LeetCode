#https://leetcode.com/problems/valid-parentheses/
#time O(N) space O(N)
class Solution:
    def isValid(self, s: str) -> bool:
        map = {']':'[',')':'(','}':'{'}
        stack = []
        for c in s:
            if c not in map:
                stack.append(c)
                continue
            if not stack or map[c]!=stack[-1]:
                return False
            stack.pop()
        return len(stack)==0
            

