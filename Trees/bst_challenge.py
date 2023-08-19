#Problem: Implement a binary search tree with an insert method.

Constraints
Can we insert None values?
No
Can we assume we are working with valid integers?
Yes
Can we assume all left descendents <= n < all right descendents?
Yes
Do we have to keep track of the parent nodes?
This is optional
Can we assume this fits in memory?
Yes

Test Cases
Insert
Insert will be tested through the following traversal:
In-Order Traversal
5, 2, 8, 1, 3 -> 1, 2, 3, 5, 8
1, 2, 3, 4, 5 -> 1, 2, 3, 4, 5
If the root input is None, return a tree with the only element being the new root node.
You do not have to code the in-order traversal, it is part of the unit test.


time O(log N) for balanced tree, O(N) worst case
space O(log N), O(N) worst case
class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Bst(object):
    root = None
    def inorder(self,node,data):
        if node is None:
            return Node(data)
        if node.data>=data:
            if not node.left:
                node.left = Node(data)
            else:
                node.left = self.inorder(node.left,data)
        else:
            if not node.right:
                node.right = Node(data)
            else:
                node.right = self.inorder(node.right,data)
        return node
        
        
    def insert(self, data):
        if data is None:
            self.root = None
            return self.root
        self.root = self.inorder(self.root,data)
        return self.root
    
