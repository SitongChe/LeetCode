#https://leetcode.com/problems/sort-list/description/
#time O(N), space O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self,l1,l2):
        dummyHead = ListNode()
        prev = dummyHead
        while l1 and l2:
            if l1.val<l2.val:
                val = l1.val
                l1 = l1.next
            else:
                val = l2.val
                l2 = l2.next
            node = ListNode(val)
            prev.next = node
            prev = node
        if l1:
            prev.next = l1
        elif l2:
            prev.next = l2
        return dummyHead.next

    def findMid(self,head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid


    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        mid = self.findMid(head)
        l2 = self.sortList(mid)
        l1 = self.sortList(head)
        
        return self.merge(l1,l2)
