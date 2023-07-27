#https://leetcode.com/problems/rotate-list/description/
#time O(N), space O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        if not head:
            return None
        cur = head
        while cur:
            cur = cur.next
            n+=1
        k = k%n
        if k == 0:
            return head
        # find n-k-1th node
        cur = head
        for i in range(n-k-1):
            cur = cur.next
        next = cur.next
        cur.next = None
        cur = next
        while cur.next:
            cur = cur.next
        cur.next = head
        return next
