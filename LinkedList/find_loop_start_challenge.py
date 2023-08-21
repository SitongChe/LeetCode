#Problem: Find the start of a linked list loop.

Constraints
Is this a singly linked list?
Yes
Can we assume we are always passed a circular linked list?
No
When we find a loop, do we return the node or the node's data?
The node
Can we assume we already have a linked list class that can be used for this problem?
Yes

Test Cases
Empty list -> None
Not a circular linked list -> None
One element
Two or more elements
Circular linked list general case

Complexity:
Time: O(n)
Space: O(1)

class MyLinkedList(LinkedList):

    def find_loop_start(self):
        if self.head is None:
            return None
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        cur = self.head
        while cur!=slow:
            slow = slow.next
            cur = cur.next
        return cur
