#https://leetcode.com/problems/reverse-linked-list/
#time O(N), space O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        cur = head
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
