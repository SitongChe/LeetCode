#Problem: Partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.

Constraints
Can we assume this is a non-circular, singly linked list?
Yes
Do we expect the function to return a new list?
Yes
Can we assume the input x is valid?
Yes
Can we assume we already have a linked list class that can be used for this problem?
Yes
Can we create additional data structures?
Yes
Can we assume this fits in memory?
Yes

Test Cases
Empty list -> []
One element list -> [element]
Left linked list is empty
Right linked list is empty
General case
Partition = 10
Input: 4, 3, 7, 8, 10, 1, 10, 12
Output: 4, 3, 7, 8, 1, 10, 10, 12

Complexity:
Time: O(n)
Space: O(n)
class MyLinkedList(LinkedList):

    def partition(self, data):
        if data is None or self.head is None:
            return None
        dummyHead = Node(None)
        prev = dummyHead
        dummyHead2 = Node(None)
        prev2 = dummyHead2
        cur = self.head
        while cur:
            if cur.data<data:
                prev.next = cur
                prev = prev.next
            elif cur.data == data:
                dummyHead2.next = Node(cur.data,dummyHead2.next)
            else:
                prev2.next = cur
                prev2 = prev2.next
            cur = cur.next
        prev.next = dummyHead2.next
        return LinkedList(dummyHead.next)
            
