#Problem: Check if a binary tree is balanced.

Constraints
Is a balanced tree one where the heights of two sub trees of any node doesn't differ by more than 1?
Yes
If this is called on a None input, should we raise an exception?
Yes
Can we assume we already have a Node class with an insert method?
Yes
Can we assume this fits memory?
Yes

Test Cases
None -> No
1 -> Yes
5, 3, 8, 1, 4 -> Yes
5, 3, 8, 9, 10 -> No
 
time O(n)
space O(h)

class BstBalance(Bst):
    def height(self,node):
        if self.ans == False:
            return 0
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        left = self.height(node.left)
        right = self.height(node.right)
        maxHeight = max(left,right)
        if maxHeight > min(left,right)+1:
            self.ans = False
        return maxHeight+1
        

    def check_balance(self):
        if self.root is None:
            raise TypeError
        self.ans = True
        self.height(self.root)
        return self.ans
