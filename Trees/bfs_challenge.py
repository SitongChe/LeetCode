#Problem: Implement breadth-first traversal on a binary tree.

Constraints
Can we assume we already have a Node class with an insert method?
Yes
Can we assume this fits in memory?
Yes
What should we do with each node when we process it?
Call an input method visit_func on the node

Test Cases
Breadth-First Traversal
5, 2, 8, 1, 3 -> 5, 2, 8, 1, 3


Complexity:
Time: O(n)
Space: O(n), extra space for the queue
class BstBfs(Bst):

    def bfs(self, visit_func):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            visit_func(cur.data)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
