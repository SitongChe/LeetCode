#Problem: Implement a binary search tree with insert, delete, different traversals & max/min node values

Constraints
Is this a binary tree?
Yes
Is the root set to None initially?
Yes
Do we care if the tree is balanced?
No
What do we return for the traversals?
Return a list of the data in the desired order
What type of data can the tree hold?
Assume the tree only takes ints. In a realistic example, we'd use a hash table to convert other types to ints.

Test Cases
Insert
Always start with the root
If value is less than the root, go to the left child
if value is more than the root, go to the right child
Delete
Deleting a node from a binary tree is tricky. Make sure you arrange the tree correctly when deleting a node.
Here are some basic instructions
If the value to delete isn't on the tree return False
Traversals
In order traversal - left, center, right
Pre order traversal - center, left, right
Post order traversal - left, right, center
Return list for all traversals
Max & Min
Find the max node in the binary search tree
Find the min node in the binary search tree
treeIsEmpty
check if the tree is empty


class Node (object):
    def __init__ (self, data=None):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__ (self):
        return str(self.data)
        
class BinaryTree (object):
    def __init__ (self):
        self.root = None
        
    def _insert(self,root,data):
        if root.data<data:
            if not root.right:
                root.right = Node(data)
            else:
                self._insert(root.right,data)
        else:
            if not root.left:
                root.left = Node(data)
            else:
                self._insert(root.left,data)
            
Time complexity: O(log(n))
Space complexity: O(n)

    def insert (self, newData):
        node = Node(newData)
        if not self.root:
            self.root=node
        else:
            self._insert(self.root,newData)
#             cur = self.root
#             prev = self.root
#             while cur:
#                 prev = cur
#                 if cur.data<newData:
#                     cur = cur.right
#                 else:
#                     cur = cur.left
#             if prev.data<newData:
#                 prev.right = node
#             else:
#                 prev.left = node
    
    def _delete(self,root,key):
        if not root:
            return None
        if key<root.data:
            root.left = self._delete(root.left,key)
        elif key>root.data:
            root.right = self._delete(root.right,key)
        else:
            self.ans = True
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                cur = root.right
                while cur.left:
                    cur = cur.left
                root.data = cur.data
                root.right = self._delete(root.right,cur.data)
        return root

Time complexity: O(log(n))
Space complexity: O(n)

    def delete (self, key):
        if not self.root:
            return False
        self.ans = False
        self.root = self._delete(self.root,key)
        return self.ans
            
Time complexity: O(log(n))
Space complexity: O(n)
    def maxNode (self):
        cur = self.root
        while cur.right:
            cur = cur.right
        return cur.data
 
 
Time complexity: O(log(n))
Space complexity: O(n)
    def minNode (self):
        cur = self.root
        while cur.left:
            cur = cur.left
        return cur.data
 
 
Time complexity: O(n) for all traversals
Space complexity: O(n)

    def printPostOrder (self):
        stack = [[self.root,False]]
        ans = []
        while stack:
            cur,visited = stack.pop()
            if cur:
                if visited:
                    ans.append(cur.data)
                else:
                    stack.append([cur,True])
                    stack.append([cur.right,False])
                    stack.append([cur.left,False])
        return ans
    
    def printPreOrder (self):
        stack = [[self.root,False]]
        ans = []
        while stack:
            cur,visited = stack.pop()
            if cur:
                if visited:
                    ans.append(cur.data)
                else:
                    stack.append([cur.right,False])
                    stack.append([cur.left,False])
                    stack.append([cur,True])
        return ans
    
    def printInOrder (self):
        stack = [[self.root,False]]
        ans = []
        while stack:
            cur,visited = stack.pop()
            if cur:
                if visited:
                    ans.append(cur.data)
                else:
                    stack.append([cur.right,False])
                    stack.append([cur,True])
                    stack.append([cur.left,False])
        return ans
    
    def treeIsEmpty (self):
        return self.root is None

