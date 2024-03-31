#Problem: Implement SetOfStacks that wraps a list of stacks, where each stack is bound by a capacity.

Constraints
Can we assume we already have a stack class that can be used for this problem?
Yes
Are all stack bound by the same capacity?
Yes
If a stack becomes full, should automatically create one?
Yes
If a stack becomes empty, should we delete it?
Yes
If we pop on an empty stack, should we return None?
Yes
Can we assume this fits memory?
Yes

Test Cases
Push and pop on an empty stack
Push and pop on a non-empty stack
Push on a capacity stack to create a new one
Pop on a stack to destroy it


class StackWithCapacity(Stack):

    def __init__(self, top=None, capacity=10):
        #self.stack = [top]*capacity
        super(StackWithCapacity, self).__init__(top)
        self.capacity=capacity
        self.index = 0

    def push(self, data):
        if self.is_full():
            raise Exception('Stack full')
        #self.stack[self.index]=data
        super(StackWithCapacity, self).push(data)
        self.index+=1

    def pop(self):
        self.index-=1
        return super(StackWithCapacity, self).pop()
#         val = self.stack[self.index]
#         self.stack[self.index]=None
#         return val

    def is_full(self):
        return self.index == self.capacity
    
    def is_empty(self):
        return self.index == 0


class SetOfStacks(object):

    def __init__(self, indiv_stack_capacity):
        self.stacks = []
        self.indiv_stack_capacity = indiv_stack_capacity

Complexity:
Time: O(1)
Space: O(m), where m is the size of the new stack if the last stack is full

    def push(self, data):
        if not self.stacks or self.stacks[-1].is_full():
            self.stacks.append(StackWithCapacity(None,self.indiv_stack_capacity))
        self.stacks[-1].push(data)

Complexity:
Time: O(1)
Space: O(1)

    def pop(self):
        if not self.stacks or self.stacks[-1].is_empty():
            return None
        val = self.stacks[-1].pop()
        if self.stacks[-1].is_empty():
            self.stacks.pop()
        return val
