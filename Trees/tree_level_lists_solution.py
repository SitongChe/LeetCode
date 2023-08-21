#Problem: Create a list for each level of a binary tree.

Constraints
Is this a binary search tree?
Yes
Should each level be a list of nodes?
Yes
Can we assume we already have a Node class with an insert method?
Yes
Can we assume this fits memory?
Yes

Test Cases
5, 3, 8, 2, 4, 1, 7, 6, 9, 10, 11 -> [[5], [3, 8], [2, 4, 7, 9], [1, 6, 10], [11]]
Note: Each number in the result is actually a node containing the number


Complexity:
Time: O(n)
Space: O(n)

class BstLevelLists(Bst):

    def create_level_lists(self):
        if not self.root:
            return None
        ans = []
        queue = [self.root]
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                cur = queue.pop(0)
                level.append(cur.data)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            ans.append(level)
                
        return ans
