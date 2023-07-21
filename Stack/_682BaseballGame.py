#https://leetcode.com/problems/baseball-game/description/
#time O(n) space O(N)
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        n = len(operations)
        if n == 0:
            return 0
        stack = []
        for operation in operations:
            if operation == "C":
                if stack:
                    stack.pop()
            elif operation == "D":
                if stack:
                    stack.append(stack[-1]*2)
            elif operation == "+":
                if len(stack)>=2:
                    stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(operation))
        return sum(stack)

