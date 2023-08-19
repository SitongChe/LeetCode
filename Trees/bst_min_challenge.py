#Problem: Create a binary search tree with minimal height from a sorted array.

Constraints
Is the array in increasing order?
Yes
Are the array elements unique?
Yes
Can we assume we already have a Node class with an insert method?
Yes
Can we assume this fits memory?
Yes

Test Cases
0, 1, 2, 3, 4, 5, 6 -> height 3
0, 1, 2, 3, 4, 5, 6, 7 -> height 4


time O(n)
space O(log N)
class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class MinBst(object):

    def create_min_bst(self, array):
        if not array:
            return None
        n = len(array)
        root = Node(array[n//2])
        root.left = self.create_min_bst(array[:n//2])
        root.right = self.create_min_bst(array[n//2+1:])
        return root
