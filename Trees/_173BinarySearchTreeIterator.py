#https://leetcode.com/problems/binary-search-tree-iterator/description/
#The time complexity of the next and hasNext operations is O(1) on average because each element is visited and processed once. The space complexity of the iterator is O(h), where h is the height of the BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def inorder(self,root):
        if not root:
            return None
        while root:
            self.stack.append(root)
            root = root.left

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.inorder(root)

    def next(self) -> int:
        cur = self.stack.pop()
        self.inorder(cur.right)
        return cur.val
  
    def hasNext(self) -> bool:
        return self.stack


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
