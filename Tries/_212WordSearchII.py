#https://leetcode.com/problems/word-search-ii/
#time O(m * n * L * W), space trie tree O(L * W), ans O(W)
class TreeNode:
    def __init__(self):
        self.isWord = False
        self.chars = {}
        self.ref = 0
class Trie:
    def __init__(self):
        self.root = TreeNode()
    def addWord(self,word):
        cur = self.root
        cur.ref +=1
        for w in word:
            if w not in cur.chars:
                cur.chars[w]=TreeNode()
            cur = cur.chars[w]
            cur.ref +=1
        cur.isWord = True
    def removeWord(self,word):
        cur = self.root
        cur.ref -=1
        for w in word:
            cur = cur.chars[w]
            cur.ref -=1
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])
        def traceback(i,j,cur,tmp,visited):
            if i<0 or i>=m or j<0 or j>=n or visited[i][j] or board[i][j] not in cur.chars or cur.ref <1:
                return
            visited[i][j]=True
            w = board[i][j]
            tmp += w
            cur = cur.chars[w]
            if cur.isWord:
                cur.isWord = False
                trie.removeWord(tmp)
                self.ans.append(tmp)
            traceback(i-1,j,cur,tmp,visited)
            traceback(i+1,j,cur,tmp,visited)
            traceback(i,j-1,cur,tmp,visited)
            traceback(i,j+1,cur,tmp,visited)
            visited[i][j]=False
        self.ans = []
        trie = Trie()
        for word in words:
            trie.addWord(word)
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.root.chars:
                    visited = [[False]*n for i in range(m)]
                    traceback(i,j,trie.root,"",visited)
        return self.ans
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
