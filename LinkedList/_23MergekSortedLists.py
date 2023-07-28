#https://leetcode.com/problems/merge-k-sorted-lists/
#time O(N * log(N)), space O(log(N))

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(l1,l2):
            dummyHead = ListNode()
            prev = dummyHead
            while l1 and l2:
                if l1.val<l2.val:
                    prev.next = l1
                    l1 = l1.next
                else:
                    prev.next = l2
                    l2 = l2.next
                prev = prev.next
            if l1:
                prev.next = l1
            if l2:
                prev.next = l2
            return dummyHead.next
        n = len(lists)
        if n == 0:
            return None
        while len(lists)>1:
            size = len(lists)
            newLists = []
            for i in range(0,size-1,2):
                newLists.append(mergeTwoLists(lists[i],lists[i+1]))
            if size%2:
                newLists.append(lists[-1])
            lists = newLists
        return lists[0]

        



