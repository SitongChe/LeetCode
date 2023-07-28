#https://leetcode.com/problems/insertion-sort-list/description/
#time O(n^2), space O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummyHead = ListNode()
        cur = head
        while cur:
            prev = dummyHead
            while prev and prev.next and prev.next.val<=cur.val:
                prev = prev.next
            next = cur.next
            cur.next = prev.next
            prev.next = cur
            cur = next
        return dummyHead.next

        

        
