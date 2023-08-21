#Problem: Find the lowest common ancestor in a binary tree.

Constraints
Is this a binary search tree?
No
Can we assume the two nodes are in the tree?
No
Can we assume this fits memory?
Yes

Test Cases
          _10_
        /      \
       5        9
      / \      / \
     12  3    18  20
        / \       /
       1   8     40
0, 5 -> None
5, 0 -> None
1, 8 -> 3
12, 8 -> 5
12, 40 -> 10
9, 20 -> 9
3, 5 -> 5


Complexity:
Time: O(h), where h is the height of the tree
Space: O(h), where h is the recursion depth

class BinaryTree(object):
    def hasNode(self,root,node):
        if not root:
            return False
        if root == node:
            return True
        return self.hasNode(root.left,node) or self.hasNode(root.right,node)
    
    def _lca(self,root,node1,node2):
        if not root:
            return None
        if root == node1 or root == node2:
            return root
        left = self._lca(root.left,node1,node2)
        right = self._lca(root.right,node1,node2)
        if not left:
            return right
        if not right:
            return left
        return root
        

    def lca(self, root, node1, node2):
        if root is None:
            raise TypeError
        if not self.hasNode(root,node1) or not self.hasNode(root,node2):
            return None
        return self._lca(root,node1,node2)
        
        
