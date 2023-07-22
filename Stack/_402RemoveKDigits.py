#https://leetcode.com/problems/remove-k-digits/description/
#time O(n) space O(N)
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while k>0 and stack and stack[-1]>c:
                stack.pop()
                k-=1
            stack.append(c)
        stack = stack[:len(stack)-k]
        ans = "".join(stack).lstrip('0')
        return ans if ans else "0"
