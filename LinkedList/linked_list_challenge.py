#Problem: Implement a linked list with insert, append, find, delete, length, and print methods.

Constraints
Can we assume this is a non-circular, singly linked list?
Yes
Do we keep track of the tail or just the head?
Just the head
Can we insert None values?
No

Test Cases
Insert to Front
Insert a None
Insert in an empty list
Insert in a list with one element or more elements
Append
Append a None
Append in an empty list
Insert in a list with one element or more elements
Find
Find a None
Find in an empty list
Find in a list with one element or more matching elements
Find in a list with no matches
Delete
Delete a None
Delete in an empty list
Delete in a list with one element or more matching elements
Delete in a list with no matches
Length
Length of zero or more elements
Print
Print an empty list
Print a list with one or more elements

Complexity:
Time: O(n)
Space: O(1)

class Node(object):

    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return str(self.data)


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head
        
    def __len__(self):
        ans = 0
        cur = self.head
        while cur:
            cur = cur.next
            ans+=1
        return ans
            

    def insert_to_front(self, data):
        if data is None:
            return
        node = Node(data)
        node.next = self.head
        self.head = node

    def append(self, data):
        if data is None:
            return
        node = Node(data)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node
            

    def find(self, data):
        if data is None or self.head is None:
            return None
        cur = self.head
        ans = []
        while cur:
            if cur.data == data:
                ans.append(cur)
            cur = cur.next
        return data if ans else None

    def delete(self, data):
        if data is None or self.head is None:
            return None
        while self.head.data == data:
            self.head = self.head.next
        cur = self.head
        while cur and cur.next:
            while cur and cur.next and cur.next.data == data:
                cur.next = cur.next.next
            cur = cur.next

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def get_all_data(self):
        cur = self.head
        ans = []
        while cur:
            ans.append(cur.data)
            cur = cur.next
        return ans
