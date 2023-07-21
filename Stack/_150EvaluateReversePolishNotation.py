#https://leetcode.com/problems/evaluate-reverse-polish-notation/
#time O(N) space O(N)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        stack = []
        for token in tokens:
            if token == '+':
                if len(stack)>=2:
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num1+num2)
            elif token == '-':
                if len(stack)>=2:
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num2-num1)
            elif token == '*':
                if len(stack)>=2:
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(num2*num1)
            elif token == '/':
                if len(stack)>=2:
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(int(num2/num1))
            else:
                stack.append(int(token))
        return stack[0] if stack else 0


