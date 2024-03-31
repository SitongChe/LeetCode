#Problem: Implement a queue with enqueue and dequeue methods using a linked list.

Constraints
If there is one item in the list, do you expect the first and last pointers to both point to it?
Yes
If there are no items on the list, do you expect the first and last pointers to be None?
Yes
If you dequeue on an empty queue, does that return None?
Yes
Can we assume this fits memory?
Yes

Test Cases
Enqueue
Enqueue to an empty queue
Enqueue to a non-empty queue
Dequeue
Dequeue an empty queue -> None
Dequeue a queue with one element
Dequeue a queue with more than one element

Complexity:
Time: O(1)
Space: O(1)

class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Queue(object):

    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def enqueue(self, data):
        node = Node(data)
        prev = self.head
        next = self.head.next
        node.prev = prev
        node.next = next
        prev.next = node
        next.prev = node

    def dequeue(self):
        node = self.tail.prev
        if node == self.head:
            return None
        next = self.tail
        prev = node.prev
        prev.next = next
        next.prev = prev
        return node.data
