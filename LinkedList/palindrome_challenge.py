#Problem: Determine if a linked list is a palindrome.

Constraints
Can we assume this is a non-circular, singly linked list?
Yes
Is a single character or number a palindrome?
No
Can we assume we already have a linked list class that can be used for this problem?
Yes
Can we use additional data structures?
Yes
Can we assume this fits in memory?
Yes

Test Cases
Empty list -> False
Single element list -> False
Two or more element list, not a palindrome -> False
General case: Palindrome with even length -> True
General case: Palindrome with odd length -> True

Complexity:
Time: O(n)
Space: O(1)
class MyLinkedList(LinkedList):
    def reverse(self,head):
        if not head or not head.next:
            return head
        last = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return last
    
    def is_palindrome(self):
        if not self.head or not self.head.next:
            return False
        fast = self.head
        slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        l2 = self.reverse(slow)
        l1 = self.head
        while l1 and l2:
            if l1.data!=l2.data:
                return False
            l1 = l1.next
            l2 = l2.next
        return True
