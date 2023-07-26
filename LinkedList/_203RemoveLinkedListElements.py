#https://leetcode.com/problems/remove-linked-list-elements/description/
#time O(N), space O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyHead = ListNode()
        dummyHead.next = head
        prev = dummyHead
        cur = head
        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = prev.next
            cur = prev.next
        return dummyHead.next
