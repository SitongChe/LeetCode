#https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
#time O(N), space O(logN) (height of the tree)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        data = []
        def preorder(root):
            if not root:
                data.append("N")
                return
            data.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ",".join(data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = data.split(",")
        self.index = 0
        def preorder():
            if vals[self.index]=="N":
                self.index+=1
                return
            root = TreeNode(vals[self.index])
            self.index+=1
            root.left = preorder()
            root.right = preorder()
            return root
        return preorder()
