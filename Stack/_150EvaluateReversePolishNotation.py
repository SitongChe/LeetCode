#https://leetcode.com/problems/evaluate-reverse-polish-notation/
#time O(N) space O(N)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                val = stack[-1]+stack[-2]
                stack.pop()
                stack.pop()
                stack.append(val)
            elif token == '-':
                val = stack[-2]-stack[-1]
                stack.pop()
                stack.pop()
                stack.append(val)
            elif token == '*':
                val = stack[-2]*stack[-1]
                stack.pop()
                stack.pop()
                stack.append(val)
            elif token == '/':
                val = int(stack[-2]/stack[-1])
                stack.pop()
                stack.pop()
                stack.append(val)
            else:
                stack.append(int(token))
        return stack[0]


