#Problem: Remove duplicates from a linked list.

Constraints
Can we assume this is a non-circular, singly linked list?
Yes
Can you insert None values in the list?
No
Can we assume we already have a linked list class that can be used for this problem?
Yes
Can we use additional data structures?
Implement both solutions
Can we assume this fits in memory?
Yes

Test Cases
Empty linked list -> []
One element linked list -> [element]
General case with no duplicates
General case with duplicates

Complexity:
Time: O(n)
Space: O(n)
class MyLinkedList(LinkedList):

    def remove_dupes_1(self):
        if not self.head:
            return
        if not self.head.next:
            return
        cur = self.head
        visited = set()
        while cur and cur.next:
            visited.add(cur.data)
            while cur and cur.next and cur.next.data in visited:
                cur.next = cur.next.next
            cur = cur.next
            
    def remove_dupes(self):
        if not self.head:
            return
        if not self.head.next:
            return
        cur = self.head
        visited = set()
        while cur and cur.next:
            visited.add(cur.data)
            if cur.next.data in visited:
                cur.next = cur.next.next
            else:
                cur = cur.next
            
                
            
