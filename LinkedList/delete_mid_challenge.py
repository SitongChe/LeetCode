#Problem: Delete a node in the middle, given only access to that node.

Constraints
Can we assume this is a non-circular, singly linked list?
Yes
What if the final node is being deleted, do we make it a dummy with value None?
Yes
Can we assume we already have a linked list class that can be used for this problem?
Yes

Test Cases
Delete on empty list -> None
Delete None -> None
Delete on one node -> [None]
Delete on multiple nodes

Complexity:
Time: O(1)
Space: O(1)

class MyLinkedList(LinkedList):

    def delete_node(self, node):
        if node is None:
            return None
        if node.next is None:
            node.data = None
        else:
            node.data = node.next.data
            node.next = node.next.next
            
