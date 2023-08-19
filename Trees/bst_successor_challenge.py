#Problem: Find the in-order successor of a given node in a binary search tree.

Constraints
If there is no successor, do we return None?
Yes
If the input is None, should we throw an exception?
Yes
Can we assume we already have a Node class that keeps track of parents?
Yes
Can we assume this fits memory?
Yes

Test Cases
          _5_
        /     \
       3       8
      / \    /   \
     2   4  6    12
    /        \   / \
   1          7 10  15
               /
              9

In: None  Out: Exception
In: 4     Out: 5
In: 5     Out: 6
In: 8     Out: 9
In: 15    Out: None

time O(h)
space O(1)

class BstSuccessor(object):

    def get_next(self, node):
        if node is None:
            raise TypeError
        if not node.right:
            while node.parent and node.parent.right == node:
                node = node.parent
            if not node.parent:
                return None
            return node.parent.data
        cur = node.right
        while cur.left:
            cur=cur.left
        return cur.data
