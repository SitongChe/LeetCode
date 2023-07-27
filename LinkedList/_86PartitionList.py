#https://leetcode.com/problems/partition-list/description/
#time O(N), space O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummyHead = ListNode(-1,head)
        prev = dummyHead
        cur = head
        largerDummyHead = ListNode()
        largerPrev = largerDummyHead
        while cur:
            if cur.val >= x:
                largerPrev.next = cur
                largerPrev = cur
            else:
                prev.next = cur
                prev = cur
            cur = cur.next
        largerPrev.next = None
        prev.next = largerDummyHead.next
        return dummyHead.next
