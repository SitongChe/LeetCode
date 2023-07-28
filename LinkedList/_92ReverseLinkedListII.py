#https://leetcode.com/problems/reverse-linked-list-ii/description/
#time O(N), space O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseTopN(self,head,n):
        if n == 1:
            self.end = head.next
            return head
        last = self.reverseTopN(head.next,n-1)
        head.next.next = head
        head.next = self.end
        return last
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        if left == 1:
            self.end = None
            return self.reverseTopN(head,right)
        else:
            head.next = self.reverseBetween(head.next,left-1,right-1)
        return head
        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummyHead = ListNode(0,head)
        prev = dummyHead
        cur = head
        for i in range(left-1):
            prev = cur
            cur = cur.next
        
        p = prev
        c = cur
        for i in range(right-left+1):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        p.next = prev
        c.next = next
        return dummyHead.next





