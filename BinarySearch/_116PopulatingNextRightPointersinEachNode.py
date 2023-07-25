#https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
#time get O(n), space O(n)
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        queue = [root]
        while queue:
            size = len(queue)
            prev = None
            for i in range(size):
                cur = queue.pop(0)
                if prev:
                    prev.next = cur
                prev = cur
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return root

                
