#https://leetcode.com/problems/linked-list-cycle-ii/description/
#time O(n), space O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        found = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                found = True
                break
        if not found:
            return None
        cur = head
        while cur:
            if cur == slow:
                return slow
            cur = cur.next
            slow = slow.next
    



