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
        def reverse(node):
            if not node or not node.next:
                return node
            l = reverse(node.next)
            node.next.next = node
            node.next = None
            return l

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        last = reverse(slow.next)
        slow.next = None
        cur = head
        while last:
            next = cur.next
            next2 = last.next
            cur.next = last
            last.next = next
            cur = next
            last = next2



