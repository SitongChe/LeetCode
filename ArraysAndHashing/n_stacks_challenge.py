#Problem: Implement n stacks using a single array.

Constraints
Are the stacks and array a fixed size?
Yes
Are the stacks equally sized?
Yes
Does pushing to a full stack result in an exception?
Yes
Does popping from an empty stack result in an exception?
Yes
Can we assume the user passed in stack index is valid?
Yes
Can we assume this fits memory?
Yess

Test Cases
Test the following on the three stacks:
Push to full stack -> Exception
Push to non-full stack
Pop on empty stack -> Exception
Pop on non-empty stack

Complexity:
Time: O(1)
Space: O(1)

class Stacks(object):

    def __init__(self, num_stacks, stack_size):
        self.stacks = [[None]*stack_size for _ in range(num_stacks)]
        self.indexs = [stack_size-1]*num_stacks
        self.stack_size = stack_size

    def push(self, stack_index, data):
        if self.indexs[stack_index]==0:
            raise Exception
        self.indexs[stack_index]-=1
        self.stacks[stack_index][self.indexs[stack_index]]=data
        

    def pop(self, stack_index):
        if self.indexs[stack_index]==self.stack_size-1:
            raise Exception
        val = self.stacks[stack_index][self.indexs[stack_index]]
        self.stacks[stack_index][self.indexs[stack_index]] = None
        self.indexs[stack_index]+=1
        return val
