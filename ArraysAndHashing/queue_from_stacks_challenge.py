#Problem: Implement a queue using two stacks.

Constraints
Do we expect the methods to be enqueue and dequeue?
Yes
Can we assume we already have a stack class that can be used for this problem?
Yes
Can we push a None value to the Stack?
No
Can we assume this fits memory?
Yes

Test Cases
Enqueue and dequeue on empty stack
Enqueue and dequeue on non-empty stack
Multiple enqueue in a row
Multiple dequeue in a row
Enqueue after a dequeue
Dequeue after an enqueue


class Solution(object):

class QueueFromStacks(object):

    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

Complexity:
Time: O(n)
Space: O(1)

    def shift_stacks(self, source, destination):
        while not source.is_empty():
            destination.push(source.pop())

Complexity:
Time: O(1)
Space: O(1)

    def enqueue(self, data):
        self.inStack.push(data)

Complexity:
Time: O(n)
Space: O(n)

    def dequeue(self):
        if self.outStack.is_empty():
            self.shift_stacks(self.inStack,self.outStack)
        return self.outStack.pop()
