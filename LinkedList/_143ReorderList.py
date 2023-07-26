#https://leetcode.com/problems/reorder-list/
#time O(N), space O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverse(head):
            if not head or not head.next:
                return head
            prev = None
            cur = head
            while cur:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
            return prev
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        l1 = head
        l2 = reverse(slow.next)
        slow.next = None
        while l2:
            next1 = l1.next
            next2 = l2.next
            l1.next = l2
            l2.next = next1
            l1 = next1
            l2 = next2


