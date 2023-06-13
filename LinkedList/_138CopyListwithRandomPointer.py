#https://leetcode.com/problems/copy-list-with-random-pointer/
#time O(N), space O(1)

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        cur = head
        while cur:
            copy = Node(cur.val)
            copy.next = cur.next
            cur.next = copy
            cur = cur.next.next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        copy = head.next
        cur = copy
        while cur and cur.next:
            cur.next = cur.next.next
            cur = cur.next
        return copy



