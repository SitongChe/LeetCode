#https://leetcode.com/problems/palindrome-linked-list/description/
#time O(N), space O(N)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head):
            if not head or not head.next:
                return head
            last = reverse(head.next)
            head.next.next = head
            head.next = None
            return last
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        l1 = head
        l2 = reverse(slow)
        while l1 and l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return True
