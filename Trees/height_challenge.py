#Problem: Determine the height of a tree.

Constraints
Is this a binary tree?
Yes
Can we assume we already have a Node class with an insert method?
Yes
Can we assume this fits memory?
Yes

Test Cases
5 -> 1
5, 2, 8, 1, 3 -> 3


Complexity:
Time: O(n)
Space: O(h), where h is the height of the tree

class BstHeight(Bst):

    def height(self, node):
        if not node:
            return 0
        return 1+max(self.height(node.left),self.height(node.right))
