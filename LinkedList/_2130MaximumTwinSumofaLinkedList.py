#https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/
#time O(N), space O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
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
        l1 = head
        l2 = reverse(slow)
        ans = 0
        while l2:
            ans = max(ans,l1.val+l2.val)
            l1 = l1.next
            l2 = l2.next
        return ans
