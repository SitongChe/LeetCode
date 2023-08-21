#Problem: Find the kth to last element of a linked list.

Constraints
Can we assume this is a non-circular, singly linked list?
Yes
Can we assume k is a valid integer?
Yes
If k = 0, does this return the last element?
Yes
What happens if k is greater than or equal to the length of the linked list?
Return None
Can you use additional data structures?
No
Can we assume we already have a linked list class that can be used for this problem?
Yes

Test Cases
Empty list -> None
k is >= the length of the linked list -> None
One element, k = 0 -> element
General case with many elements, k < length of linked list

Complexity:
Time: O(n)
Space: O(1)

class MyLinkedList(LinkedList):

    def kth_to_last_elem_1(self, k):
        if self.head is None:
            return None
        n = self.__len__()
        if k>n:
            return None
        cur = self.head
        
        for _ in range(n-1-k):
            cur = cur.next
        return cur.data
    
    def kth_to_last_elem(self, k):
        if self.head is None:
            return None
        fast = self.head
        for _ in range(k):
            fast = fast.next
            if not fast:
                return None
        slow = self.head
        while fast.next:
            fast = fast.next
            slow = slow.next
        return slow.data
            
