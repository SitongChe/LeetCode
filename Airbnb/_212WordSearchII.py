#https://leetcode.com/problems/word-search-ii/description/
#time O(m * n * 4^L + W * L) space O(W * L)
class TreeNode:
    def __init__(self):
        self.isWord = False
        self.chars = {}
        self.ref = 0
class TrieTree:
    def __init__(self):
        self.root = TreeNode()
    def addWord(self,word):
        cur = self.root
        for w in word:
            cur.ref+=1
            if w not in cur.chars:
                cur.chars[w] = TreeNode()
            cur = cur.chars[w]
        cur.ref+=1
        cur.isWord = True
    def removeWord(self,word):
        cur = self.root
        for w in word:
            cur.ref-=1
            cur = cur.chars[w]
        cur.ref-=1
        cur.isWord = False
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def traceback(cur,i,j,tmp):
            if cur.isWord:
                tree.removeWord(tmp)
                ans.append(tmp)
            if i<0 or i>=m or j<0 or j>=n or (i,j) in visited or board[i][j] not in cur.chars or cur.ref<1:
                return
            visited.add((i,j))
            tmp += board[i][j]
            traceback(cur.chars[board[i][j]],i+1,j,tmp)
            traceback(cur.chars[board[i][j]],i-1,j,tmp)
            traceback(cur.chars[board[i][j]],i,j+1,tmp)
            traceback(cur.chars[board[i][j]],i,j-1,tmp)
            visited.remove((i,j))
            tmp=tmp[:-1]
 
        m = len(board)
        n = len(board[0])
        ans = []
        tree = TrieTree()
        for word in words:
            tree.addWord(word)
        for i in range(m):
            for j in range(n):
                if board[i][j] in tree.root.chars:
                    visited = set()
                    traceback(tree.root,i,j,"")
        return ans

