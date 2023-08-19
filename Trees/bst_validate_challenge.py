#Problem: Determine if a tree is a valid binary search tree.

Constraints
Can the tree have duplicates?
Yes
If this is called on a None input, should we raise an exception?
Yes
Can we assume we already have a Node class?
Yes
Can we assume this fits in memory?
Yes

Test Cases
Valid:
      5
    /   \
   5     8
  /     /
 4     6
        \
         7
        
Invalid:
      5
    /   \
   5     8
  / \   /
 4   9 7
 
time O(n)
space O(h)

class BstValidate(Bst):
    def inorder(self,node):
        if not node:
            return True
        if not self.inorder(node.left):
            return False
        if self.prev and node.data<self.prev:
            return False
        self.prev = node.data
        return self.inorder(node.right)

    def validate(self):
        if self.root is None:
            raise TypeError
        self.prev = None
        return self.inorder(self.root)
