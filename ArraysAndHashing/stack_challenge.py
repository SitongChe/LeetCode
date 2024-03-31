#Problem: Implement a stack with push, pop, peek, and is_empty methods using a linked list.

Constraints
If we pop on an empty stack, do we return None?
Yes
Can we assume this fits memory?
Yes

Test Cases
Push
Push to empty stack
Push to non-empty stack
Pop
Pop on empty stack
Pop on single element stack
Pop on multiple element stack
Peek
Peek on empty stack
Peek on one or more element stack
Is Empty
Is empty on empty stack
Is empty on one or more element stack

Complexity:
Time: O(1)
Space: O(1)

class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack(object):

    def __init__(self, top=None):
        self.head = top

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def pop(self):
        if not self.head:
            return None
        val = self.head.data
        self.head = self.head.next
        return val

    def peek(self):
        return self.head.data if self.head else None

    def is_empty(self):
        return self.head is None
