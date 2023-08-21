#Problem: Add two numbers whose digits are stored in a linked list in reverse order.

Constraints
Can we assume this is a non-circular, singly linked list?
Yes
Do we expect the return to be in reverse order too?
Yes
What if one of the inputs is None?
Return None for an invalid operation
How large are these numbers--can they fit in memory?
Yes
Can we assume we already have a linked list class that can be used for this problem?
Yes
Can we assume this fits in memory?
Yes

Test Cases
Empty list(s) -> None
Add values of different lengths
Input 1: 6->5->None
Input 2: 9->8->7
Result: 5->4->8
Add values of same lengths
Exercised from values of different lengths
Done here for completeness


class MyLinkedList(LinkedList):

    def add_reverse(self, first_list, second_list):
        if first_list is None or second_list is None:
            return None
        carry = 0
        dummyHead = Node(0)
        prev = dummyHead
        first_list = first_list.head
        second_list = second_list.head
        while first_list or second_list or carry:
            cur = (first_list.data if first_list else 0) +(second_list.data if second_list else 0) +carry
            carry = cur//10
            prev.next = Node(cur%10)
            prev = prev.next
            if first_list:
                first_list = first_list.next
            if second_list:
                second_list = second_list.next
        return MyLinkedList(dummyHead.next)
