#Problem: Implement a stack with push, pop, and min methods running O(1) time.

Constraints
Can we assume this is a stack of ints?
Yes
Can we assume the input values for push are valid?
Yes
If we call this function on an empty stack, can we return sys.maxsize?
Yes
Can we assume we already have a stack class that can be used for this problem?
Yes
Can we assume this fits memory?
Yes

Test Cases
Push/pop on empty stack
Push/pop on non-empty stack
Min on empty stack
Min on non-empty stack

Complexity:
Time: O(1)
Space: O(1)

# %load ../stack/stack.py
class Node(object):

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack(object):

    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        self.top = Node(data, self.top)

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        return self.top.data if self.top is not None else None

    def is_empty(self):
        return self.peek() is None




import sys


class StackMin(Stack):

    def __init__(self, top=None):
        super(StackMin, self).__init__(top)
        self.minValueStack = Stack(top)

    def minimum(self):
        val = self.minValueStack.peek()
        if val is None:
            val = sys.maxsize
        return val

    def push(self, data):
        super(StackMin, self).push(data)
        if data<self.minimum():
            self.minValueStack.push(data)

    def pop(self):
        data = super(StackMin, self).pop()
        if data==self.minimum():
            self.minValueStack.pop()
        return data
