#https://leetcode.com/problems/merge-k-sorted-lists/
#time O(N * log(N)), space O(log(N))

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def mergeTwoLists(l1, l2):
            dummyHead = ListNode()
            prev = dummyHead
            while l1 and l2:
                if l1.val<l2.val:
                    prev.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    prev.next = ListNode(l2.val)
                    l2 = l2.next
                prev = prev.next
            if l1:
                prev.next = l1
            if l2:
                prev.next = l2
            return dummyHead.next
        while len(lists)>1:
            n = len(lists)
            newList = []
            for i in range(n//2):
                l = mergeTwoLists(lists[i],lists[n-i-1])
                newList.append(l)
            if n%2:
                newList.append(lists[n//2])
            lists = newList
        return lists[0]
        



