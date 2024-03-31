#Problem: Sort a stack. You can use another stack as a buffer.

Constraints
When sorted, should the largest element be at the top or bottom?
Top
Can you have duplicate values like 5, 5?
Yes
Can we assume we already have a stack class that can be used for this problem?
Yes
Can we assume this fits memory?
Yes

Test Cases
Empty stack -> None
One element stack
Two or more element stack (general case)
Already sorted stack

Complexity:
Time: O(n^2)
Space: O(n)

class MyStack(Stack):

    def sort(self):
        buffer = Stack()
        while not self.is_empty():
            cur = self.pop()
            if buffer.is_empty() or cur>=buffer.peek():
                buffer.push(cur)
            else:
                while not buffer.is_empty() and buffer.peek()>cur:
                    self.push(buffer.pop())
                buffer.push(cur)
        return buffer
        
class MyStackSimplified(Stack):

    def sort(self):
        buff = MyStack()
        while not self.is_empty():
            temp = self.pop()
            while not buff.is_empty() and temp < buff.peek():
                self.push(buff.pop())
            buff.push(temp)
        return buff
