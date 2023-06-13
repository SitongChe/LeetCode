#https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#time O(N), space O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #remove the length - n - 1th node
        dummyHead = ListNode(0,head)
        cur = head
        prev = dummyHead
        for i in range(n):
            cur = cur.next
        while cur:
            prev = prev.next
            cur = cur.next
        prev.next = prev.next.next
        return dummyHead.next




