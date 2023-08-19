#Problem: Invert a binary tree.

Constraints
What does it mean to invert a binary tree?
Swap all left and right node pairs
Can we assume we already have a Node class?
Yes
Can we assume the inputs are valid?
No
Can we assume this fits memory?
Yes

Test Cases
Input:
     5
   /   \
  2     7
 / \   / \
1   3 6   9

Output:
     5
   /   \
  7     2
 / \   / \
9   6 3   1


Complexity:
Time: O(n)
Space: O(h), where h is the height, for the recursion depth

class GraphShortestPath(Graph):

class InverseBst(Bst):
    def _invert_tree(self,node):
        if not node:
            return None
        node.left,node.right = self._invert_tree(node.right),self._invert_tree(node.left)
        return node
    def invert_tree(self):
        if not self.root:
            raise TypeError
        return self._invert_tree(self.root)
