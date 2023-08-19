#Problem: Find the second largest node in a binary search tree.

Constraints
If this is called on a None input or a single node, should we raise an exception?
Yes
None -> TypeError
Single node -> ValueError
Can we assume we already have a Node class with an insert method?
Yes
Can we assume this fits memory?
Yes

Test Cases
None or single node -> Exception
Input:
                _10_
              _/    \_
             5        15
            / \       / \
           3   8     12  20
          /     \         \
         2       4        30

Output: 20

Input:
                 10
                 /
                5
               / \
              3   7
Output: 7


time O(h)
space O(1)

class Solution(Bst):
    def find_second_largest(self):
        if not self.root:
            raise TypeError
        if not self.root.left and self.root.right:
            raise ValueError
        prev = None
        cur = self.root
        if cur.right is None:
            cur = cur.left
            while cur:
                prev = cur
                cur = cur.right
        else:
            while cur.right:
                prev = cur
                cur = cur.right
        return prev
        
