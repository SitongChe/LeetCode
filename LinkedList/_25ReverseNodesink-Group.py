#https://leetcode.com/problems/reverse-nodes-in-k-group/
#time O(max(N, M)), space O(max(N, M))

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyHead = ListNode(0,head)
        prev = dummyHead
        while True:
            p = prev
            c = prev.next
            cur = prev.next
            for i in range(k):
                if not cur:
                    return dummyHead.next
                cur = cur.next
            cur = prev.next
            for i in range(k):
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
         
            p.next.next = cur
            p.next = prev
            prev = c
        return dummyHead.next
        
        
            
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseTopK(self,head,k):
        prev = None
        cur = head
        for i in range(k):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev

    def findKth(self,cur,k):
        for i in range(k):
            if not cur:
                return [False,None]
            cur = cur.next
        return [True,cur]

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        found,kth = self.findKth(head,k)
        if not found:
            return head
        last = self.reverseTopK(head,k)
        head.next = self.reverseKGroup(kth,k)
        return last
        
        

        

        
