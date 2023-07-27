#https://leetcode.com/problems/swap-nodes-in-pairs/description/
#time O(N), space O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(-1,head)
        prev = dummyHead
        cur = head
        while cur and cur.next:
            node1 = cur
            node2 = cur.next
            next = node2.next
            prev.next = node2
            node2.next = node1
            node1.next = next
            prev = node1
            cur = next
        return dummyHead.next

